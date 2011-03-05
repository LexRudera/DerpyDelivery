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

import objects
from derpyDelivery import cfg
from objects.base import base
import pygame

#handles objects
class handler():

	def __init__(self):
		self.bgImage = None
		self.bgRepeat = (False, False)
		self.dimensions = (0, 0)
		self.pauseObject = None
		self.currentRoom = None
		cfg.keyH.assignKeyPress(pygame.K_ESCAPE, self.pause)
	
	def pause(self):
		if cfg.objH.pause():
			self.pauseObject = cfg.objH.new(objects.optionsMenu)
		else:
			self.pauseObject.destroy()
			
	def clearRoom(self):
		while len(base.instances) > 0:
			instance = base.instances[0]
			instance.destroy()
			
	def mainMenu(self):
		self.currentRoom = self.mainMenu
		self.bgImage = cfg.imgH.file["bg_menu"][0]
		self.bgRepeat = (True, True)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.mainMenuController)
		
	def introCutscene(self):
		self.currentRoom = self.introCutscene
		self.bgImage = None
		self.bgRepeat = (False, False)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.introCutsceneController)
		
	def stageOne(self):
		self.currentRoom = self.stageOne
		print cfg.imgH.file["bg_stage1"][0]
		self.bgImage = cfg.imgH.file["bg_stage1"][0]
		self.bgRepeat = (False, False)
		self.dimensions = (4000, 1200)
		#stop music
		if cfg.sndH.currentLoop is not None:
			cfg.sndH.stop(cfg.sndH.currentLoop)
		#room bounding blocks
		cfg.objH.new(objects.dynamicBlock, (0, -32), (self.dimensions[0], 70))
		cfg.objH.new(objects.dynamicBlock, (0, self.dimensions[1]-50), (self.dimensions[0], 100))
		cfg.objH.new(objects.dynamicBlock, (-32, 0), (64, self.dimensions[1]-50))
		cfg.objH.new(objects.dynamicBlock, (self.dimensions[0]-32, 0), (32, self.dimensions[1]-50))
		#
		d = cfg.objH.new(objects.derpy, (2300, 300))
		#mail
		cfg.objH.new(objects.mail, (2000, 1000))
		cfg.objH.new(objects.mail, (1000, 1000))
		birdMail = cfg.objH.new(objects.mail, (3400, 400))
		#bushes
		cfg.objH.new(objects.bush, (1000, 1100), "env_bush_spiky")
		cfg.objH.new(objects.bush, (3000, 1100), "env_bush_spiky")
		cfg.objH.new(objects.bush, (3800, 1100), "env_bush_spiky")
		#bird
		b = cfg.objH.new(objects.birdWithMail, (2700, 400), birdMail)
		b.speedMod = 1.5
		cfg.objH.new(objects.birdWithMail, (2900, 200), None)
		b = cfg.objH.new(objects.birdWithMail, (3400, 500), None)
		b.speedMod = 1.2
		cfg.objH.new(objects.birdWithMail, (3300, 300), None).dir = -1
		b = cfg.objH.new(objects.birdWithMail, (3335, 500), None)
		b.speedMod = .9
		b = cfg.objH.new(objects.birdWithMail, (3600, 350), None)
		b.dir = -1
		b.speedMod = .7
		#boxbrown
		cfg.objH.new(objects.boxBrown, (2400, 250), d)
		
		
	def testRoom(self):
		self.currentRoom = self.testRoom
		self.bgImage = cfg.imgH.file["bg_test"][0]
		self.bgRepeat = (True, True)
		self.dimensions = (1000, 1000)
		#room bounding blocks
		cfg.objH.new(objects.dynamicBlock, (0, -32), (self.dimensions[0], 32))
		cfg.objH.new(objects.dynamicBlock, (0, self.dimensions[1]), (self.dimensions[0], 32))
		cfg.objH.new(objects.dynamicBlock, (-32, 0), (32, self.dimensions[1]))
		cfg.objH.new(objects.dynamicBlock, (self.dimensions[0], 0), (32, self.dimensions[1]))
		#
		cfg.objH.new(objects.crate, (100, 400))
		cfg.objH.new(objects.crate, (164, 400))
		cfg.objH.new(objects.crate, (228, 400))
		cfg.objH.new(objects.crate, (280, 400))
		cfg.objH.new(objects.crate, (350, 400))
		cfg.objH.new(objects.crate, (410, 400))
		cfg.objH.new(objects.crate, (480, 400))
		cfg.objH.new(objects.crate, (540, 400))
		cfg.objH.new(objects.derpy, (15, 15))