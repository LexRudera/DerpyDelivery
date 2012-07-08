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
		cfg.sndH.loop("music_title")
		cfg.objH.new(objects.mainMenuController)
		
	def stageIntro(self, stageNumber, stageName, stageObjective, stageTar):
		self.currentRoom = self.stageIntro
		self.bgImage = cfg.imgH.file["bg_stagestart"][0]
		self.bgRepeat = (False, False)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.startStage, stageNumber, stageName, stageObjective, stageTar)
		
	def stageComplete(self, stageNumber, bonuses, stageTar):
		self.currentRoom = self.stageComplete
		self.bgImage = cfg.imgH.file["bg_stageend"][0]
		self.bgRepeat = (False, False)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.endStage, stageNumber, bonuses, stageTar)
		
	def introCutscene(self):
		self.currentRoom = self.introCutscene
		self.bgImage = None
		self.bgRepeat = (False, False)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.introCutsceneController)
		
	def stageTwoCutscene(self):
		self.currentRoom = self.stageTwoCutscene
		self.bgImage = None
		self.bgRepeat = (False, False)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.stageTwoCutsceneController)
		
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
		d = cfg.objH.new(objects.derpy, (2300, 300), False)
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
		
		
	def stageTwo(self):
		self.currentRoom = self.stageTwo
		self.bgImage = None
		self.bgRepeat = (False, False)
		self.dimensions = (8000, 2000)
		#room bounding blocks
		cfg.objH.new(objects.dynamicBlock, (-32, -80), (self.dimensions[0]+64, 80))
		cfg.objH.new(objects.dynamicBlock, (-32, self.dimensions[1]-32), (self.dimensions[0]+64, 96))
		cfg.objH.new(objects.dynamicBlock, (-80, -32), (80, self.dimensions[1]+64))
		cfg.objH.new(objects.dynamicBlock, (self.dimensions[0], -32), (80, self.dimensions[1]+64))
		sk = objects.scoreKeeperStage2()
		#road
		t = cfg.objH.new(objects.base, (4000, 1547), "bg_stage2_road", False, True)
		t.depth = 999
		#clouds
		c = cfg.objH.new(objects.base, (500, 200), "bg_stage2_clouds_big", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (2700, 550), "bg_stage2_clouds_big", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6200, 400), "bg_stage2_clouds_big", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (0, 800), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (3200, 200), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (1700, 300), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (4800, 900), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6500, 150), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (7300, 560), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (200, 560), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (700, 920), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (1350, 820), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (1600, 200), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (2150, 345), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (2743, 639), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (3967, 274), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (4376, 748), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (4932, 275), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (5923, 832), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6389, 433), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6904, 322), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (7290, 439), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (7904, 328), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (0, 1300), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (3200, 1200), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (1700, 1300), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6500, 1150), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (7300, 1560), "bg_stage2_clouds_med", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (200, 1560), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (1600, 1200), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (2150, 1345), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (2743, 1639), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (3967, 1274), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (4376, 1748), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (4932, 1275), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (5923, 1832), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6389, 1433), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (6904, 1322), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (7290, 1439), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		c = cfg.objH.new(objects.base, (7904, 1328), "bg_stage2_clouds_small", False, True)
		c.depth = 1000
		#derpy
		derpy = cfg.objH.new(objects.derpy, (1, 1600))
		derpy.impulse((1000, 0))
		#daisy
		flowers = []
		flowers.append(cfg.objH.new(objects.flower, (400, 1900), "flower_white"))
		flowers.append(cfg.objH.new(objects.flower, (500, 1910), "flower_red"))
		flowers.append(cfg.objH.new(objects.flower, (600, 1920), "flower_white"))
		flowers.append(cfg.objH.new(objects.flower, (450, 1905), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (300, 1923), "flower_blue"))
		flowers.append(cfg.objH.new(objects.flower, (200, 1934), "flower_white"))
		flowers.append(cfg.objH.new(objects.flower, (260, 1898), "flower_white"))
		flowers.append(cfg.objH.new(objects.flower, (580, 1902), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (680, 1924), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (623, 1900), "flower_blue"))
		flowers.append(cfg.objH.new(objects.flower, (286, 1910), "flower_purple"))
		flowers.append(cfg.objH.new(objects.flower, (512, 1920), "flower_red"))
		flowers.append(cfg.objH.new(objects.flower, (237, 1905), "flower_blue"))
		flowers.append(cfg.objH.new(objects.flower, (186, 1923), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (283, 1934), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (529, 1898), "flower_red"))
		flowers.append(cfg.objH.new(objects.flower, (686, 1902), "flower_white"))
		flowers.append(cfg.objH.new(objects.flower, (326, 1924), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (437, 1905), "flower_blue"))
		flowers.append(cfg.objH.new(objects.flower, (386, 1923), "flower_purple"))
		flowers.append(cfg.objH.new(objects.flower, (483, 1934), "flower_pink"))
		flowers.append(cfg.objH.new(objects.flower, (329, 1898), "flower_red"))
		flowers.append(cfg.objH.new(objects.flower, (486, 1902), "flower_blue"))
		flowers.append(cfg.objH.new(objects.flower, (426, 1924), "flower_purple"))
		
		cfg.objH.new(objects.daisy, (400, 1880), flowers, sk)
		#mayor
		g = cfg.objH.new(objects.mayor, (4000, 1930), sk)
		cfg.objH.new(objects.mailAlert, g, derpy, (68, -68))
		#clocktower
		t = cfg.objH.new(objects.base, (1050, 1365), "env_stage2_houses_clocktower", False, True)
		t.depth = 25
			#dr hooves
		g = cfg.objH.new(objects.drhooves, (1050, 800), sk)
		cfg.objH.new(objects.mailAlert, g, derpy)
		#deckhouse
		t = cfg.objH.new(objects.base, (1800, 1672), "env_stage2_houses_deckhouse", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (1780, 1750), "env_stage2_houses_deckhouse_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (1780, 1750), "env_stage2_houses_deckhouse_interior", False, True)
		t.depth = 100
			#interior stuff
		t = cfg.objH.new(objects.horte, (1540, 1850))
		t.depth = 45
		t = cfg.objH.new(objects.rndm, (1500, 1800), "env_table_thin", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (1840, 1800), "env_table", 3)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (1990, 1800), "env_table", 3)
		t.swapLayer(2)
		t.depth = 50
			#walls
		cfg.objH.new(objects.depthBlock, (1700, 1430), (470, 135))
		cfg.objH.new(objects.depthBlock, (2130, 1550), (60, 180))
		cfg.objH.new(objects.depthBlock, (1390, 1720), (320, 50))
		cfg.objH.new(objects.depthBlock, (1390, 1770), (35, 140))
		cfg.objH.new(objects.depthBlock, (1390, 1910), (830, 40))
			#converters
		cfg.objH.new(objects.depthConverter, (1680, 1640), 150)
		cfg.objH.new(objects.depthConverter, (2190, 1810), 150, True)
		#profileshop
		t = cfg.objH.new(objects.base, (2878, 1606), "env_stage2_houses_profileshop", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (2900, 1827), "env_stage2_houses_profileshop_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (2900, 1822), "env_stage2_houses_profileshop_interior", False, True)
		t.depth = 100
			#interior stuff
		t = cfg.objH.new(objects.rndm, (2750, 1800), "env_table", 3)
		t.swapLayer(2)
		t.depth = 50
			#walls
		cfg.objH.new(objects.depthBlock, (2660, 1710), (520, 40))
		cfg.objH.new(objects.depthBlock, (2600, 1740), (90, 40))
		cfg.objH.new(objects.depthBlock, (2600, 1910), (580, 20))
		cfg.objH.new(objects.depthBlock, (3100, 1740), (30, 170))
			#converters
		cfg.objH.new(objects.depthConverter, (2620, 1840), 130)
		#school
		t = cfg.objH.new(objects.base, (3620, 1560), "env_stage2_houses_school", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (3640, 1680), "env_stage2_houses_school_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (3640, 1544), "env_stage2_houses_school_interior", False, True)
		t.depth = 100
			#interior stuff
		tt = cfg.objH.new(objects.rndm, (3600, 1710), "env_table_desk", 3)
		tt.swapLayer(2)
		tt.depth = 50
		t = cfg.objH.new(objects.cheerilee, (3500, 1680), tt, sk)
		t.swapLayer(2)
		t.depth = 50
		g = cfg.objH.new(objects.mailAlert, t, derpy, (68, -68))
		g.swapLayer(2)
		g.alpha = 127
		t = cfg.objH.new(objects.rndm, (3650, 1700), "sweetiebell_sit", 2, tt, "sweetiebell_sit_suprised", True)
		t.swapLayer(2)
		t.depth = 50
		tt = cfg.objH.new(objects.rndm, (3730, 1710), "env_table_desk", 3)
		tt.swapLayer(2)
		tt.depth = 50
		t = cfg.objH.new(objects.rndm, (3780, 1700), "scootaloo_sit", 2, tt, "scootaloo_sit_suprised", True)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (3830, 1710), "env_table_desk", 3)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (3880, 1710), "env_chair", 2)
		t.swapLayer(2)
		t.depth = 50
			#walls
		cfg.objH.new(objects.depthBlock, (3490, 1320), (250, 20))
		cfg.objH.new(objects.depthBlock, (3490, 1330), (35, 240))
		cfg.objH.new(objects.depthBlock, (3680, 1330), (30, 240))
		cfg.objH.new(objects.depthBlock, (3330, 1570), (270, 20))
		cfg.objH.new(objects.depthBlock, (3720, 1570), (200, 20))
		cfg.objH.new(objects.depthBlock, (3340, 1580), (30, 160))
		cfg.objH.new(objects.depthBlock, (3880, 1580), (30, 160))
		cfg.objH.new(objects.depthBlock, (3330, 1730), (620, 40))
			#converters
		cfg.objH.new(objects.depthPortal, (3605, 1420))
		#fancy
		t = cfg.objH.new(objects.base, (4240, 1685), "env_stage2_houses_fancy", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (4240, 1730), "env_stage2_houses_fancy_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (4234, 1740), "env_stage2_houses_fancy_interior", False, True)
		t.depth = 100
			#interior
		t = cfg.objH.new(objects.rndm, (4180, 1720), "env_table_thin", 2)
		t.swapLayer(2)
		t.depth = 50
		t1 = cfg.objH.new(objects.rndm, (4180, 1660), "env_vase_white", 1)
		t1.swapLayer(2)
		t1.depth = 50
		t = cfg.objH.new(objects.rndm, (4300, 1720), "env_table_thin", 2)
		t.swapLayer(2)
		t.depth = 50
		t2 = cfg.objH.new(objects.rndm, (4290, 1660), "env_vase_white", 1)
		t2.swapLayer(2)
		t2.depth = 50
		#lily
		cfg.objH.new(objects.lily, (4120, 1830), [t1, t2], sk)
			#walls
		cfg.objH.new(objects.depthBlock, (4080, 1610), (300, 20))
		cfg.objH.new(objects.depthBlock, (4080, 1620), (35, 150))
		cfg.objH.new(objects.depthBlock, (4355, 1620), (35, 150))
		cfg.objH.new(objects.depthBlock, (4080, 1750), (300, 20))
			#converters
		cfg.objH.new(objects.depthPortal, (4240, 1700))
		#thatch
		t = cfg.objH.new(objects.base, (4760, 1690), "env_stage2_houses_thatch", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (4795, 1655), "env_stage2_houses_thatch_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (4795, 1655), "env_stage2_houses_thatch_interior", False, True)
		t.depth = 100
			#interior stuff
		t = cfg.objH.new(objects.rndm, (4800, 1700), "env_crate", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (4800, 1700), "env_crate", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (4800, 1700), "env_crate", 2)
		t.swapLayer(2)
		t.depth = 50
			#walls
		cfg.objH.new(objects.depthBlock, (4480, 1680), (200, 20))
		cfg.objH.new(objects.depthBlock, (4480, 1780), (530, 20))
		cfg.objH.new(objects.depthBlock, (4900, 1570), (30, 240))
		cfg.objH.new(objects.depthBlock, (4660, 1570), (35, 110))
		cfg.objH.new(objects.depthBlock, (4660, 1570), (350, 30))
			#converters
		cfg.objH.new(objects.depthConverter, (4480, 1740), 80)
		#bakery
		t = cfg.objH.new(objects.base, (5290, 1690), "env_stage2_houses_bakery", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (5280, 1708), "env_stage2_houses_bakery_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (5284, 1728), "env_stage2_houses_bakery_interior", False, True)
		t.depth = 100
		#
		t = cfg.objH.new(objects.mscake, (5240, 1830))
		t.depth = 51
		#oven
		cfg.objH.new(objects.oven, (5155, 1800))
		g = cfg.objH.new(objects.cookingMailbag, (5110, 1820), sk)
		#smoke
		cfg.objH.new(objects.smokeMaker, (5130, 1500), g)
			#walls
		cfg.objH.new(objects.depthBlock, (5310, 1540), (200, 25))
		cfg.objH.new(objects.depthBlock, (5440, 1560), (95, 350))
		cfg.objH.new(objects.depthBlock, (5400, 1700), (100, 20))
		cfg.objH.new(objects.depthBlock, (5300, 1570), (35, 130))
		cfg.objH.new(objects.depthBlock, (5000, 1720), (135, 200))
		cfg.objH.new(objects.depthBlock, (5115, 1900), (400, 40))
		cfg.objH.new(objects.depthBlock, (5090, 1700), (220, 30))
		#interior
		t = cfg.objH.new(objects.rndm, (5450, 1600), "env_crate", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5450, 1600), "env_crate", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5450, 1600), "env_crate", 2)
		t.swapLayer(2)
		t.depth = 50
		#door
		bd = cfg.objH.new(objects.bakeryDoor, (5418, 1850))
			#converters
		cfg.objH.new(objects.depthPortal, (5425, 1870), bd)
		#suprised
		t = cfg.objH.new(objects.base, (5800, 1600), "env_stage2_houses_suprised", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (5790, 1664), "env_stage2_houses_suprised_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (5798, 1666), "env_stage2_houses_suprised_interior", False, True)
		t.depth = 1000
		#interior stuff
		t = cfg.objH.new(objects.rndm, (5660, 1750), "env_vase_white", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5690, 1750), "env_vase_red", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5720, 1750), "env_vase_white", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5750, 1750), "env_vase_pink", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5780, 1750), "env_vase_white", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5810, 1750), "env_vase_red", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5840, 1750), "env_vase_white", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5870, 1750), "env_vase_pink", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5900, 1750), "env_vase_red", 2)
		t.swapLayer(2)
		t.depth = 50
		t = cfg.objH.new(objects.rndm, (5930, 1750), "env_vase_white", 2)
		t.swapLayer(2)
		t.depth = 50
			#walls
		cfg.objH.new(objects.depthBlock, (5600, 1420), (400, 30))
		cfg.objH.new(objects.depthBlock, (5600, 1450), (30, 420))
		cfg.objH.new(objects.depthBlock, (5970, 1450), (30, 420))
		cfg.objH.new(objects.depthBlock, (5600, 1870), (400, 30))
		cfg.objH.new(objects.depthBlock, (5630, 1730), (110, 20))
		cfg.objH.new(objects.depthBlock, (5840, 1730), (120, 20))
		cfg.objH.new(objects.depthBlock, (5630, 1560), (240, 20))		
			#converters
		cfg.objH.new(objects.depthPortal, (5700, 1660))
		cfg.objH.new(objects.depthPortal, (5880, 1660))
		#applebloom
		t = cfg.objH.new(objects.appleSign, (6150, 1850))
		f = cfg.objH.new(objects.appleStand, (6150, 1850), t)
		cfg.objH.new(objects.applebloom, (6070, 1920), derpy, f, sk)
		#plaza
		t = cfg.objH.new(objects.base, (6800, 1710), "env_stage2_houses_plaza", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (6284, 1705), "env_stage2_houses_plaza_windows_left", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (6820, 1695), "env_stage2_houses_plaza_windows_mid", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (7130, 1790), "env_stage2_houses_plaza_windows_right", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (6720, 1735), "env_stage2_houses_plaza_interior", False, True)
		t.depth = 100
		#lyra & bonbon
		t = cfg.objH.new(objects.rndm, (7100, 1936), "env_table", 2)
		t.swapLayer(3)
		t.depth = -50
		t.body.moment = 10000
		t = cfg.objH.new(objects.rndm, (7100, 1890), "env_plateofhay", 1)
		t.swapLayer(3)
		t.depth = -50
		tt = cfg.objH.new(objects.muffin, (7070, 1900), "env_muffin_green")
		tt.swapLayer(3)
		tt.depth = -50
		t = cfg.objH.new(objects.rndm, (7000, 1920), "lyra_stand_r", 2, tt, "lyra_cry_r", True, "lyra_cry_r", (sk, "lyraCry"))
		t.swapLayer(2)
		t.depth = -20
		t.imageSpeed = .1
		tt = cfg.objH.new(objects.muffin, (7130, 1900), "env_muffin_brown")
		tt.swapLayer(3)
		tt.depth = -50
		t = cfg.objH.new(objects.rndm, (7200, 1920), "bonbon_stand_l", 2, tt, "bonbon_mad_l", True, "bonbon_mad_l", (sk, "bonbonMad"))
		t.swapLayer(2)
		t.depth = -20
			#walls
		cfg.objH.new(objects.depthBlock, (6170, 1620), (500, 20))
		cfg.objH.new(objects.depthBlock, (6170, 1760), (400, 20))
		cfg.objH.new(objects.depthBlock, (6170, 1630), (35, 130))
		cfg.objH.new(objects.depthBlock, (6500, 1730), (35, 30))
		cfg.objH.new(objects.depthBlock, (6500, 1620), (35, 30))
			#converters
		cfg.objH.new(objects.depthConverter, (6550, 1690), 80, True)
		cfg.objH.new(objects.depthConverter, (6500, 1690), 80, True)
		#end 
		t = cfg.objH.new(objects.base, (7771, 1680), "env_stage2_houses_end", False, True)
		t.depth = 25
		t = cfg.objH.new(objects.base, (7810, 1655), "env_stage2_houses_end_windows", False, True)
		t.depth = 40
		t.alpha = 100
		t = cfg.objH.new(objects.base, (7810, 1655), "env_stage2_houses_end_interior", False, True)
		t.depth = 100
		
	
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