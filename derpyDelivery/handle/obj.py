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
import json
import os
import types

#handles objects
class handler():
	
	def __init__(self):
		#load fonts
		self.veryLargeText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 34)
		self.largeText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 22)
		self.mediumText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 14)
		self.smallText = pygame.font.Font(os.path.join(os.path.abspath('font'), "font.ttf"), 10)
		#create camera
		self.cam = camera()
		#pause
		self.paused = False
		self.keyReleasePrePause = {}
		self.keyDownPrePause = {}
		self.keyPressPrePause = {}
		#framespeed
		self.frameSpeed = 1
		self.defFS = 30
		#stage scores
		self.stageScores = {}
	
	#create new object
	#	arguments:
	#		objectType 	- new object class to create
	#		*args		- arguments for the new object class' __init__
	#	returns:
	#		newObject - the object created
	def new(self, objectType, *args):
		newObject = objectType(*args)
		return newObject
	
	def saveSettings(self):
		controls = {
			"right"		: cfg.rightButton,
			"up"		: cfg.upButton,
			"left"		: cfg.leftButton,
			"down"		: cfg.downButton,
			"one"		: cfg.oneButton,
			"two"		: cfg.twoButton,
			"start"		: cfg.startButton,
			"menu"		: cfg.menuButton
		}
		sound = {
			"music" 	: str(cfg.sndH.musicVolume),
			"effects" 	: str(cfg.sndH.effectVolume),
		}
		video = {"fps" : str(self.frameSpeed)}
		settings = {
			"controls" 	: controls,
			"sound"		: sound,
			"video"		: video
		}
		f = open(os.path.abspath("config"), "w")
		jsonCfg = json.dump(settings, f)
		f.close()
		
	#pause
	def pause(self):
		self.paused = not self.paused
		if self.paused:
			#save key events for later, clear them out, but keep the pause key
			self.keyReleasedPrePause = cfg.keyH.keyRelease
			self.keyDownPrePause = cfg.keyH.keyDown
			self.keyPressPrePause = cfg.keyH.keyPress
			cfg.keyH.keyRelease = {}
			cfg.keyH.keyDown = {}
			cfg.keyH.keyPress = {}
			
			for e in self.keyReleasedPrePause:
				if self.keyReleasedPrePause[e] == cfg.rmH.pause:
					cfg.keyH.assignKeyRelease(e, cfg.rmH.pause)
			for e in self.keyDownPrePause:
				if self.keyDownPrePause[e] == cfg.rmH.pause:
					cfg.keyH.assignKeyDown(e, cfg.rmH.pause)
			for e in self.keyPressPrePause:
				if self.keyPressPrePause[e] == cfg.rmH.pause:
					cfg.keyH.assignKeyPress(e, cfg.rmH.pause)
		else:
			#re-assign keys to pre-pause mode
			cfg.keyH.keyRelease = self.keyReleasedPrePause
			cfg.keyH.keyDown = self.keyDownPrePause
			cfg.keyH.keyPress = self.keyPressPrePause
		return self.paused
	#preStep
	def preStep(self):
		for o in base.instances:
			o.preStep()
	#step
	def step(self):
		for o in base.instances:
			o.animateStep()
		for o in base.instances:
			o.step()
	#endStep
	def endStep(self):
		for o in base.instances:
			o.endStep()
	
	#draw
	def draw(self):
		#move camera
		self.cam.follow()
		#draw background, repeat it if necessary
		if cfg.rmH.bgImage is not None:
			if isinstance(cfg.rmH.bgImage, types.ListType):
				for imgDef in cfg.rmH.bgImage:
					img = imgDef[0]
					ioW = imgDef[1]
					ioH = imgDef[2]
					if self.cam.isInView((ioW, ioH), img):
						position = (ioW-self.cam.position[0], ioH-self.cam.position[1])
						cfg.window.blit(img, position)
			else:
				position = (-self.cam.position[0], -self.cam.position[1])
				cfg.window.blit(cfg.rmH.bgImage, position)
		else:
			pass
			cfg.window.fill((86,189,227))	#fill window
		#sort objects by depth
		base.instances.sort(key = lambda d: d.depth, reverse = True)
		#draw each object in order if visible
		for o in base.instances:
			if o.visible:
				if o.image is not None:
					images = o.image[o.imageIndex]												#get img
					if isinstance(images, types.ListType):
							#shredded image
						last = images[len(images)-1]
						width = last[1]+last[0].get_width()
						height = last[2]+last[0].get_height()
						center = o.body.position-self.cam.position+o.drawffset					#find object center
						camRect = pygame.rect.Rect((0, 0), (840, 525))
						imgCenter = (width/2, height/2)
						for imgDef in images:
							img = imgDef[0]
							ioW = imgDef[1]
							ioH = imgDef[2]
							if self.cam.isInView(o.body.position+o.drawffset+(ioW, ioH)-imgCenter, img):			#if in view
								if o.alpha != img.get_alpha():														
									img.set_alpha(o.alpha, pygame.RLEACCEL)
								myRect = pygame.rect.Rect(center-imgCenter+(ioW, ioH), (img.get_width(), img.get_height()))
								cliprect = camRect.clip(myRect)
								cliprect = cliprect.move(-(center-imgCenter+(ioW, ioH)))
								cfg.window.blit(img, center-imgCenter+(ioW, ioH)+(cliprect.left, cliprect.top), cliprect)
								"""testing
								pygame.draw.rect(cfg.window, (255, 0, 255), pygame.rect.Rect(center-imgCenter+(cliprect.left, cliprect.top), (img.get_width(), img.get_height())), 1)
								cliprect = cliprect.move(center[0]-imgCenter[0], center[1]-imgCenter[1])
								pygame.draw.rect(cfg.window, (255, 0, 0), cliprect, 1)
								pygame.draw.circle(cfg.window, (0, 0, 255), o.body.position-self.cam.position, 10)
								pygame.draw.circle(cfg.window, (255, 255, 0), center-imgCenter, 5)
								pygame.draw.circle(cfg.window, (255, 0, 255), center, 5)
								"""
								
					else:	#single image
						img = images
						if o.scale != 1:															#apply scale
							img = pygame.transform.scale(img, (int(img.get_width()*o.scale), int(img.get_height()*o.scale)))
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
							img.set_alpha(o.alpha)
							center = o.body.position-self.cam.position+o.drawffset						#find object center
							camRect = pygame.rect.Rect((0, 0), (840, 525))
							myRect = pygame.rect.Rect(center-imgCenter, (img.get_width(), img.get_height()))
							cliprect = camRect.clip(myRect)
							cliprect = cliprect.move(-(center-imgCenter))
							cfg.window.blit(img, center-imgCenter+(cliprect.left, cliprect.top), cliprect)
							"""testing
							cliprect = cliprect.move(center[0]-imgCenter[0], center[1]-imgCenter[1])
							pygame.draw.rect(cfg.window, (255, 0, 0), cliprect, 1)
							pygame.draw.circle(cfg.window, (255, 255, 0), center-imgCenter, 5)
							pygame.draw.circle(cfg.window, (255, 0, 255), center, 5)
							"""
						
				o.draw()
	
#handles camera
class camera():
		
		#init
		def __init__(self):
			self.position = (0, 0)
			self.__view = (cfg.window.get_width(), cfg.window.get_height())
			self.tracker = None
			self.trackingBounds = (self.__view[0]/3, self.__view[1]/3)
			
		def getRect(self):
			return pygame.rect.Rect((0,0), (840, 525))
		
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