"""
Copyright 2010 Erik Soma <stillusingirc@gmail.com>

This file is part of Derpy Delivery.

Derpy Delivery is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Derpy Delivery is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Derpy Delivery. If not, see <http://www.gnu.org/licenses/>.
"""

from base import base
from math import copysign, fabs
from derpyDelivery import cfg
import derpy
import pymunk

#64x64 crate
class crate(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_crate", True, False)
		self.body.mass = 2
		#shape
		self.addRect((0, 0), (64, 64))

#balloon
class balloon(base):

	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_balloon")
		self.body.mass = 1
		#shape
		self.addCircle(32)
		self.drawffset = (0, 32)
		
	def step(self):
		self.impulse((0, -10))
		
#mail
class mail(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_mail", True, False)
		self.body.mass = 1
		self.scale = .75
		#shape
		self.shape = self.addRect((0, 0), (29, 21))
		#derpy 
		self.derpyRef = None
		self.arrowIndex = 0
		
	def preStep(self):
		if self.body.velocity[1] > 0:
			self.body.angular_velocity += -copysign(.1, self.body.velocity[0])
		
	def requestPickup(self, other):
		self.derpyRef = other
		
	def draw(self):
		if self.derpyRef is not None:
			if self.derpyRef.canPickUp == self and self.derpyRef.pickedUp is None:
				img = cfg.imgH.file["env_pickuparrow"][self.arrowIndex]
				img.set_alpha(128)
				cfg.window.blit(img, self.body.position-cfg.objH.cam.position-(15, 35))
				self.arrowIndex += 1
				if self.arrowIndex == len(cfg.imgH.file["env_pickuparrow"]):
					self.arrowIndex = 0
					
#bush
class bush(base):

	def __init__(self, position, imgKey):
		#base init
		base.__init__(self, position, imgKey, True, True)
		self.depth = -999
		#shape
		self.shape = self.addRect((0, 30), (124, 74))
		self.imageSpeed = 0
		#derpy collision
		self.collisionEvent(derpy.derpy, bush.shake)
			
	def shake(self, other):
		if self.imageSpeed == 0:
			if (fabs(other.body.velocity[0]) + fabs(other.body.velocity[1])) > 500:
				self.imageSpeed = .25
				self.imageIndex = 1
		
	def step(self):
		if self.imageIndex == 0:
			self.imageSpeed = 0
			
#bird
class birdWithMail(base):

	def __init__(self, position, grabMail):
		base.__init__(self, position, "env_bird_red_r")
		self.shape = self.addRect((10, 5),(32, 24))
		self.imageSpeed = .3
		self.grabMail = grabMail
		if self.grabMail is not None:
			self.grabMail.sensor = True
		self.dir = 1
		self.vdir = 1.0
		self.body.mass = 3
		self.speedMod = 1
		#angle lock
		self.angleLockBody = pymunk.Body(pymunk.inf, pymunk.inf)
		self.angleLock = pymunk.constraint.RotaryLimitJoint(self.body, self.angleLockBody, 0, 0)
		cfg.space.add(self.angleLock)
		
	def step(self):
		#phase counter
		if self.body.position[0] < 2600:
			self.dir = 1
		elif self.body.position[0] > 3400:
			self.dir = -1
		if self.body.position[1] < 200:
			self.vdir = -.2
		elif self.body.position[1] > 600:
			self.vdir = -1
		self.impulse((30*self.dir*self.speedMod, 30*self.vdir))
		if self.dir == 1:
			self.setImage("env_bird_red_r")
		else:
			self.setImage("env_bird_red_l")
		#move mail
		if self.grabMail is not None:
			self.grabMail.set((self.body.position[0]+(30*self.dir), self.body.position[1]))
			if self.grabMail.derpyRef is not None:
				if self.grabMail.derpyRef.pickedUp == self.grabMail:
					self.grabMail = None
					