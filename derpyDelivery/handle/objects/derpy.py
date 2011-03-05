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

from base import base, cfg
import pygame
import pymunk
from math import pi, hypot, sin
import env
import test
from env import mail


#handles object
class derpy(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "derpy_fly_r")
		#make tracker
		cfg.objH.cam.tracker = self
		#shape
		self.addRect((0, 0), (35, 40))
		#proximity detector
		self.proxDet = self.addRect((0, 0), (80, 40))
		self.proxDet.sensor = True
		#image
		self.drawffset = (0, -20)
		self.depth = -10
		self.imageSpeed = .15
		#bind controls
		cfg.keyH.assignKeyDown(pygame.K_LEFT, self.moveLeft)
		cfg.keyH.assignKeyDown(pygame.K_RIGHT, self.moveRight)
		cfg.keyH.assignKeyDown(pygame.K_UP, self.moveUp)
		cfg.keyH.assignKeyDown(pygame.K_DOWN, self.moveDown)
		cfg.keyH.assignKeyPress(pygame.K_x, self.pickUp)
		cfg.keyH.assignKeyRelease(pygame.K_x, self.dropOff)
		#collision events
		#mail proximity
		self.collisionEvent(mail, derpy.ackPickUp)
		#speed checking
		self.lastXSpeed = 0
		self.forceRight = False
		self.forceLeft = False
		#angle lock
		self.angleLockBody = pymunk.Body(pymunk.inf, pymunk.inf)
		self.angleLock = pymunk.constraint.RotaryLimitJoint(self.body, self.angleLockBody, 0, 0)
		cfg.space.add(self.angleLock)
		#pickup
		self.canPickUp = None
		self.pickedUp = None
		#binary direction
		self.dir = 1
		
	def moveLeft(self):
		self.impulse((-300, 0))
		self.forceLeft = True
	
	def moveRight(self):
		self.impulse((300, 0))
		self.forceRight = True
		
	def moveUp(self):
		self.impulse((0, -300))
		
	def moveDown(self):
		self.impulse((0, 300))
		
	def pickedUpFollow(self):
		if self.pickedUp is not None:
			self.pickedUp.body.angle = 0
			offset = (45*self.dir, -25)
			self.pickedUp.body.position = (self.body.position[0]+offset[0], self.body.position[1]+offset[1])
		
	def pickUp(self):
		if self.canPickUp is not None:
			self.pickedUp = self.canPickUp
			self.pickedUp.shape.sensor = True
			self.pickedUp.depth = self.depth-1
			
	def dropOff(self):
		if self.pickedUp is not None:
			self.pickedUp.shape.sensor = False
			self.pickedUp.impulse(self.body.velocity)
			self.pickedUp = None
			
	def ackPickUp(self, other):
		if self.canPickUp is None:
			self.canPickUp = other
			other.requestPickup(self)
		
	def draw(self):
		pass
		"""
		p = (self.body.position[0]+self.proxDet.offset[0]-cfg.objH.cam.position[0], self.body.position[1]+self.proxDet.offset[1]-cfg.objH.cam.position[1])
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.proxDet.get_points()[0]-cfg.objH.cam.position, self.proxDet.get_points()[1]-cfg.objH.cam.position))
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.proxDet.get_points()[1]-cfg.objH.cam.position, self.proxDet.get_points()[2]-cfg.objH.cam.position))
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.proxDet.get_points()[2]-cfg.objH.cam.position, self.proxDet.get_points()[3]-cfg.objH.cam.position))
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.proxDet.get_points()[3]-cfg.objH.cam.position, self.proxDet.get_points()[0]-cfg.objH.cam.position))
		"""
	
	def preStep(self):
		self.canPickUp = None
	
	def step(self):
		#fight gravity
		self.impulse((0, -50))
		#change image
		if self.body.velocity[0] > 2 and not self.forceLeft:
			self.dir = 1
			#right
			if self.body.velocity[0] >= self.lastXSpeed:
				#print "increasing right"
				base.setImage(self, "derpy_fly_r")
			else:
				pass
				#print "slowing towards left"
		elif self.body.velocity[0] < -2 and not self.forceRight:
			self.dir = -1
			#left
			if self.body.velocity[0] <= self.lastXSpeed:
				#print "increasing left"
				base.setImage(self, "derpy_fly_l")
			else:
				pass
				#print "slowing towards right"
		#pickup
		self.pickedUpFollow()
			
	def endStep(self):
		self.forceLeft = False
		self.forceRight = False
		self.lastXSpeed = self.body.velocity[0]
		