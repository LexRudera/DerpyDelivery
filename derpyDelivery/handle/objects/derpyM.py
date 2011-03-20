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
import test
from envM import mail, muffin, oven, cookingMailbag


class givemail(base):
	def __init__(self, position, target, derpy):
		base.__init__(self, position, "env_mail", False, False)
		self.addRect((0,0), (1, 1))
		self.target = target.parent
		self.scale = .5
		self.swapLayer(3)
		self.collisionEvent(target.parent.__class__, givemail.col)
		self.derpy = derpy
		
	def step(self):
		self.body.slew(self.target.body.position, 1)
		
	def col(self, other, myShapes):
		self.derpy.delivered = True
		other.getMail()
		self.destroy()

#handles object
class derpy(base):
	
	def __init__(self, position, mailBag = True):
		#base init
		sprite = "derpy_fly_bag_r"
		if not mailBag:
			sprite = "derpy_fly_r"
		base.__init__(self, position, sprite)
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
		cfg.keyH.assignKeyDown(cfg.leftButton, self.moveLeft)
		cfg.keyH.assignKeyDown(cfg.rightButton, self.moveRight)
		cfg.keyH.assignKeyDown(cfg.upButton, self.moveUp)
		cfg.keyH.assignKeyDown(cfg.downButton, self.moveDown)
		cfg.keyH.assignKeyPress(cfg.twoButton, self.pickUp)
		cfg.keyH.assignKeyRelease(cfg.twoButton, self.dropOff)
		cfg.keyH.assignKeyPress(cfg.oneButton, self.deliverMail)
		#collision events
		#mail proximity
		self.collisionEvent(mail, derpy.ackPickUp)
		self.collisionEvent(muffin, derpy.ackPickUp)
		self.collisionEvent(cookingMailbag, derpy.ackPickUp)
		self.collisionEvent(oven, derpy.ackOpen)
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
		self.mailBag = mailBag
		self.canDeliver = None
		self.delivering = None
		self.delivered = True
		self.canOpen = None
		
	def moveLeft(self):
		if self.delivering is None:
			self.impulse((-300, 0))
			self.forceLeft = True
	
	def moveRight(self):
		if self.delivering is None:
			self.impulse((300, 0))
			self.forceRight = True
		
	def moveUp(self):
		if self.delivering is None:
			self.impulse((0, -300))
		
	def moveDown(self):
		if self.delivering is None:
			self.impulse((0, 300))
		
	def deliverMail(self):
		if self.canDeliver is not None and self.delivering is None and self.delivered:
			cfg.sndH.play("effects_threeWog")
			if self.dir == 1:
				self.setImage("derpy_fly_getmail_r")
			else:
				self.setImage("derpy_fly_getmail_l")
			self.delivering = self.canDeliver
			self.body.velocity = (0, 0)
		
	def pickedUpFollow(self):
		if self.pickedUp is not None:
			self.pickedUp.body.angle = 0
			offset = (45*self.dir, -25)
			self.pickedUp.body.position = (self.body.position[0]+offset[0], self.body.position[1]+offset[1])
		
	def pickUp(self):
		if self.canPickUp is not None:
			if  isinstance(self.canPickUp, muffin):
				self.eat(self.canPickUp)
			else:
				self.pickedUp = self.canPickUp
				self.pickedUp.shape.sensor = True
				self.pickedUp.depth = self.depth-1
		if self.canOpen is not None:
			self.canOpen.openUp()
			
	def dropOff(self):
		if self.pickedUp is not None:
			self.pickedUp.shape.sensor = False
			self.pickedUp.impulse(self.body.velocity)
			self.pickedUp = None
			
	def ackPickUp(self, other, myShapes):
		if self.canPickUp is None:
			self.canPickUp = other
			other.requestPickup(self)
		if other.__class__ == cookingMailbag:
			cookingMailbag.putOut(other, self, None)
			
	def ackOpen(self, other, myShapes):
		if not other.open:
			other.requestOpen(self)
			self.canOpen = other
			
	def eat(self, other):
		cfg.sndH.play("effects_omnomnom")
		other.destroy()
		
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
		
	def animationEnd(self):
		if self.delivering is not None:
			self.imageSpeed = .15
			if self.dir == 1:
				base.setImage(self, "derpy_fly_bag_r")
			else:
				base.setImage(self, "derpy_fly_bag_l")
			cfg.objH.new(givemail, self.body.position, self.delivering, self).depth = self.depth-1
			self.delivering = None
			self.delivered = False
	
	def step(self):
		#fight gravity
		self.impulse((0, -50))
		#change image
		if self.delivering is None:
			if self.body.velocity[0] > 100 and not self.forceLeft:
				self.dir = 1
				#right
				if self.body.velocity[0] >= self.lastXSpeed:
					#print "increasing right"
					if self.mailBag:
						base.setImage(self, "derpy_fly_bag_r")
					else:
						base.setImage(self, "derpy_fly_r")
				else:
					pass
					#print "slowing towards left"
			elif self.body.velocity[0] < -100 and not self.forceRight:
				self.dir = -1
				#left
				if self.body.velocity[0] <= self.lastXSpeed:
					#print "increasing left"
					if self.mailBag:
						base.setImage(self, "derpy_fly_bag_l")
					else:
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
		self.canDeliver = None
		