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


#handles object
class derpy(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "derpy_stand_r")
		#make tracker
		cfg.objH.cam.tracker = self
		#shape
		#self.stuffs = self.addCircle(48)
		self.stuffs = self.addRect((0, 0), (35, 40))
		self.drawffset = (0, -20)
		self.depth = -10
		self.imageSpeed = .15
		#bind controls
		cfg.keyH.assignKeyDown(pygame.K_LEFT, self.moveLeft)
		cfg.keyH.assignKeyDown(pygame.K_RIGHT, self.moveRight)
		cfg.keyH.assignKeyDown(pygame.K_UP, self.moveUp)
		cfg.keyH.assignKeyDown(pygame.K_DOWN, self.moveDown)
		cfg.keyH.assignKeyDown(pygame.K_r, self.test)
		#collision events
		self.collisionEvent(test.testBlock, self.prant)
		#speed checking
		self.lastXSpeed = 0
		self.forceRight = False
		self.forceLeft = False
		#angle lock
		self.angleLockBody = pymunk.Body(pymunk.inf, pymunk.inf)
		self.angleLock = pymunk.constraint.RotaryLimitJoint(self.body, self.angleLockBody, 0, 0)
		cfg.space.add(self.angleLock)
		
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
		
	def test(self):
		cfg.objH.new(env.balloon, (200, 100))
		
	def prant(self, other):
		pass
		#print "collide"
		
	def draw(self):
		pass
		#p = (self.body.position[0]+self.stuffs.offset[0]-cfg.objH.cam.position[0], self.body.position[1]+self.stuffs.offset[1]-cfg.objH.cam.position[1])
		#pygame.draw.circle(cfg.window, (0, 0, 0), p, 48, 1)
		#pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[0]-cfg.objH.cam.position, self.stuffs.get_points()[1]-cfg.objH.cam.position))
		#pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[1]-cfg.objH.cam.position, self.stuffs.get_points()[2]-cfg.objH.cam.position))
		#pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[2]-cfg.objH.cam.position, self.stuffs.get_points()[3]-cfg.objH.cam.position))
		#pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[3]-cfg.objH.cam.position, self.stuffs.get_points()[0]-cfg.objH.cam.position))
		
	def step(self):
		#fight gravity
		self.impulse((0, -50))
		#change image
		if self.body.velocity[0] > 2 and not self.forceLeft:
			#right
			if self.body.velocity[0] >= self.lastXSpeed:
				#print "increasing right"
				base.setImage(self, "derpy_fly_r")
			else:
				pass
				#print "slowing towards left"
		elif self.body.velocity[0] < -2 and not self.forceRight:
			#left
			if self.body.velocity[0] <= self.lastXSpeed:
				#print "increasing left"
				base.setImage(self, "derpy_fly_l")
			else:
				pass
				#print "slowing towards right"
			
	def endStep(self):
		self.forceLeft = False
		self.forceRight = False
		self.lastXSpeed = self.body.velocity[0]
		