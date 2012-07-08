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
from math import pi
import pymunk
import pygame
from derpyDelivery import cfg

#handles object
class testBlock(base):
	
	def __init__(self, position, depth):
		#base init
		base.__init__(self, position, "test_block", True, False)
		self.depth = depth
		self.alpha = 255
		self.imageSpeed = .03
		self.solid = True
		self.body.mass = 8
		#shape
		self.stuffs = self.addRect((0, 0), (64, 64))
		
	def draw(self):
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[0]-cfg.objH.cam.position, self.stuffs.get_points()[1]-cfg.objH.cam.position))
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[1]-cfg.objH.cam.position, self.stuffs.get_points()[2]-cfg.objH.cam.position))
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[2]-cfg.objH.cam.position, self.stuffs.get_points()[3]-cfg.objH.cam.position))
		pygame.draw.lines(cfg.window, (255,255,255), False, (self.stuffs.get_points()[3]-cfg.objH.cam.position, self.stuffs.get_points()[0]-cfg.objH.cam.position))
		
class testBall(base):

	def __init__(self, position):
		#base init
		base.__init__(self, position, "test_ball")
		self.solid = True
		self.body.mass = 2
		#shape
		self.stuffs = self.addCircle(32)
		
	def draw(self):
		p = (self.body.position[0]+self.stuffs.offset[0]-cfg.objH.cam.position[0], self.body.position[1]+self.stuffs.offset[1]-cfg.objH.cam.position[1])
		pygame.draw.circle(cfg.window, (0, 0, 0), p, 32, 1)