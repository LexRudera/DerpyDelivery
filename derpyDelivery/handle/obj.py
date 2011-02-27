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

import os.path
import pygame
from math import ceil, degrees, cos, sin, pi, tan, hypot, floor, radians
from derpyDelivery import cfg
from objects.base import base

#handles objects
class handler():
	
	def __init__(self):
		#load fonts
		self.largeText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 22)
		self.mediumText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 14)
		self.smallText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 10)
		self.cam = camera()
		
	def new(self, objectType, *args):
		newObject = objectType(*args)
		
	def step(self):
		for o in base.instances:
			o.preStep()
		for o in base.instances:
			o.animateStep()
		for o in base.instances:
			o.step()
		for o in base.instances:
			o.endStep()
		
	def draw(self):
		#move camera
		self.cam.follow()
		#cfg.window.fill((0,0,0))	#fill window
		#draw background
		xTimes = 0
		yTimes = 0
		bgWidth = cfg.rmH.bgImage.get_width()
		bgHeight = cfg.rmH.bgImage.get_height()
		if cfg.rmH.bgRepeat[0]:
			xTimes = int(ceil((cfg.rmH.dimensions[0]/bgWidth)))+1
		if cfg.rmH.bgRepeat[1]:
			yTimes = int(ceil((cfg.rmH.dimensions[0]/bgHeight)))+1
		for xRepeat in range(xTimes):
			for yRepeat in range(yTimes):
				position = (xRepeat*bgWidth, yRepeat*bgHeight)
				if self.cam.isInView(position, cfg.rmH.bgImage):
					position = (position[0]-self.cam.position[0], position[1]-self.cam.position[1])
					cfg.window.blit(cfg.rmH.bgImage, position)
		#sort by depth
		base.instances.sort(key = lambda d: d.depth, reverse = True)
		#draw each object in order if visible
		for o in base.instances:
			if o.visible:
				if o.image is not None:
					img = o.image[o.imageIndex]													#get img
					if o.alpha != 255:															#apply alpha
						img.set_alpha(o.alpha)
					rot = (degrees(o.body.angle)/2.0)											#apply rotation, limit to degrees of 2
					if rot < 0:
						rot = ceil(rot)
					else:
						rot = floor(rot)
					rot *= 2
					if rot != 0:
						img = pygame.transform.rotate(img, -rot)
					imgCenter = (img.get_width()/2, img.get_height()/2)							#get center
					if self.cam.isInView(o.body.position+o.drawffset-imgCenter, img):			#if in view
						center = o.body.position-self.cam.position+o.drawffset						#find object center
						cfg.window.blit(img, center-imgCenter)										#draw
				o.draw()
	
#handles camera
class camera():
		
		#init
		def __init__(self):
			self.position = (0, 0)
			self.__view = (cfg.window.get_width(), cfg.window.get_height())
			self.tracker = None
			self.trackingBounds = (self.__view[0]/3, self.__view[1]/3)
		
		#check if an image is in the view
		def isInView(self, position, img):
			imgWidth = img.get_width()
			imgHeight = img.get_height()
			#check X plane
			if self.position[0] < (position[0]+imgWidth) and self.position[0]+self.__view[0] > position[0]:
				#check Y plane
				if self.position[1] < (position[1]+imgHeight) and self.position[1]+self.__view[1] > position[1]:
					return True
			return False
		
		#follow the tracker object
		def follow(self):
			if self.tracker is not None:
				#X
				if self.position[0]+self.trackingBounds[0] > self.tracker.body.position[0]:
					self.position = (int(self.tracker.body.position[0]-self.trackingBounds[0]), self.position[1])
				elif self.position[0]+self.__view[0]-self.trackingBounds[0] < self.tracker.body.position[0]+self.tracker.image[self.tracker.imageIndex].get_width():
					self.position = (int(self.tracker.body.position[0]+self.tracker.image[self.tracker.imageIndex].get_width()-self.__view[0]+self.trackingBounds[0]), self.position[1])
				#Y
				if self.position[1]+self.trackingBounds[1] > self.tracker.body.position[1]:
					self.position = (self.position[0], int(self.tracker.body.position[1]-self.trackingBounds[1]))
				elif self.position[1]+self.__view[1]-self.trackingBounds[1] < self.tracker.body.position[1]+self.tracker.image[self.tracker.imageIndex].get_height():
					self.position = (self.position[0], int(self.tracker.body.position[1]+self.tracker.image[self.tracker.imageIndex].get_height()-self.__view[1]+self.trackingBounds[1]))
				#stay within room bounds
				if self.position[0] < 0:
					self.position = (0, self.position[1])
				elif self.position[0]+self.__view[0] > cfg.rmH.dimensions[0]:
					self.position = (cfg.rmH.dimensions[0]-self.__view[0], self.position[1])
				if self.position[1] < 1:
					self.position = (self.position[0], 0)
				elif self.position[1]+self.__view[1] > cfg.rmH.dimensions[1]:
					self.position = (self.position[0], cfg.rmH.dimensions[1]-self.__view[1])
			else:
				self.position = (0, 0)