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
from derpyDelivery import cfg
from math import floor
from envM import mailAlert
import pygame

class actor(base):
	
	def __init__(self, position, imgKey):
		#base init
		base.__init__(self, position, imgKey, False)
		
class dialog(base):
	def __init__(self, imgKey, dialogList):
		#base init
		base.__init__(self, (770, 455), imgKey, False, True)
		self.blackSurface = pygame.Surface((700, 300))
		self.blackSurface.fill((0, 0, 0))
		cfg.keyH.assignKeyPress(cfg.oneButton, self.next)
		self.dialogList = dialogList
		self.imageSpeed = .1
		self.currentDialog = 0
		self.currentCharacter = 0
		self.depth = -9999
		self.a = 255
		
	def next(self):
		totalCurrentLength = len(self.dialogList[self.currentDialog][0]) +  len(self.dialogList[self.currentDialog][1]) +  len(self.dialogList[self.currentDialog][2]) +  len(self.dialogList[self.currentDialog][3])
		if self.currentCharacter < totalCurrentLength:
			self.currentCharacter = totalCurrentLength
		else:
			self.currentDialog += 1
			self.currentCharacter = 0
			if self.currentDialog >= len(self.dialogList):
				self.visible = False
				cfg.keyH.assignKeyPress(cfg.oneButton, None)
	
	def draw(self):
		self.a -= 5
		if self.a < 130:
			self.a = 255
		if cfg.objH.frameSpeed == 1:
			self.currentCharacter += 1
		else:
			self.currentCharacter += .5
		c = int(floor(self.currentCharacter))
		cfg.window.blit(self.blackSurface, (0, 385))
		if c < len(self.dialogList[self.currentDialog][0]):
			cfg.window.blit(cfg.objH.mediumText.render(self.dialogList[self.currentDialog][0][:c], 0, (255, 255, 255)), (30, 410))
			cfg.sndH.play("interface_textblip")
		else:
			cfg.window.blit(cfg.objH.mediumText.render(self.dialogList[self.currentDialog][0], 0, (255, 255, 255)), (30, 410))
			c = c - len(self.dialogList[self.currentDialog][0])
			if c < len(self.dialogList[self.currentDialog][1]):
				cfg.window.blit(cfg.objH.mediumText.render(self.dialogList[self.currentDialog][1][:c], 0, (255, 255, 255)), (30, 440))
				cfg.sndH.play("interface_textblip")
			else:
				cfg.window.blit(cfg.objH.mediumText.render(self.dialogList[self.currentDialog][1], 0, (255, 255, 255)), (30, 440))
				c = c- len(self.dialogList[self.currentDialog][1])
				if c < len(self.dialogList[self.currentDialog][2]):
					cfg.window.blit(cfg.objH.mediumText.render(self.dialogList[self.currentDialog][2][:c], 0, (255, 255, 255)), (30, 470))
					cfg.sndH.play("interface_textblip")
				else:
					cfg.window.blit(cfg.objH.mediumText.render(self.dialogList[self.currentDialog][2], 0, (255, 255, 255)), (30, 470))
					c = c - len(self.dialogList[self.currentDialog][2])
					if c < len(self.dialogList[self.currentDialog][3]):
						cfg.window.blit(cfg.objH.smallText.render(self.dialogList[self.currentDialog][3][:c], 0, (255, 255, 255)), (30, 490))
						cfg.sndH.play("interface_textblip")
					else:
						cfg.window.blit(cfg.objH.smallText.render(self.dialogList[self.currentDialog][3], 0, (255, 255, 255)), (30, 490))
		skip = cfg.objH.smallText.render("[ "+cfg.keyH.keyCodeToString(cfg.oneButton).upper()+" ]", 0, (255, 255, 48))
		skip.set_alpha(self.a)
		cfg.window.blit(skip, (350, 515))
		
class stageTwoCutsceneController(base):
	def __init__(self):
		#base init
		base.__init__(self, (0,0), None, False, True)
		cfg.keyH.assignKeyPress(cfg.startButton, self.finish)
		#dialog box
		self.dialogBox = None
		#
		self.trig = 0
		self.timer = 0
		self.bgPos = (0, 0)
		self.bgImage = cfg.imgH.file["bg_cutscene_fsOne"][0]
		self.bgImage2 = cfg.imgH.file["bg_cutscene_fsOne_hills"][0]
		self.depth = 900
		self.bgStop = False
		#derpy actor
		self.derpy = cfg.objH.new(actor, (200, 300), "derpy_fly_bag_r")
		self.derpy.imageSpeed = .2
		#boxhorse
		self.boxBrown = cfg.objH.new(actor, (270, 250), "boxhorse_fly_r")
		self.boxBrown.depth = 5
		self.boxBrown.imageSpeed = .15
		self.boxBrown.needMail = True
		self.boxBrown.dir = 1
		self.mailAlert = None
	
	def finish(self):
		cfg.keyH.assignKeyPress(cfg.startButton, None)
		cfg.rmH.clearRoom()
		cfg.rmH.stageIntro("2", "Ponyville", ("Find the Mailbag", "Bonus: Deliver 3 Letters"), cfg.rmH.stageTwo)
		
	def step(self):
		
		if self.trig <> 4:
			self.boxBrown.set((270, 250))
			self.derpy.set((200, 300))
		if cfg.objH.frameSpeed == 1:
			self.timer += 2
			if not self.bgStop:
				self.bgPos = (self.bgPos[0]-2, 0)
		else:
			self.timer += 1
			if not self.bgStop:
				self.bgPos = (self.bgPos[0]-1, 0)
		if self.trig == 0:
			if self.timer >= 90:
				self.trig = 1
				self.timer = 0
				if int(cfg.objH.stageScores["1"][0][1]) <= 0:
					self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", [("Took you long enough to get those letters! Too", "busy playing with birds? The day just started", "and we're already behind schedule!", "...not that we've ever been on schedule.")])
				elif int(cfg.objH.stageScores["1"][0][1]) < 40:
					self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", [("I have to admit that was pretty quick. Maybe if", "you put that much effort into delivering", "letters we wouldn't be behind schedule so often!", "")])
				else:
					self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", [("You have got some sharp eyes and quick wings", "Derpy! I've never seen you move so fast. Maybe", "we will actually be on schedule today!", "...wait no I was late coming over...")])
		elif self.trig == 1:
			if not self.dialogBox.visible:
				self.trig = 2
				self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", [("Anyway...", "I have to get back to the Post Office and take", "care of some deliveries to Sweet Apple Acres.", ""), ("I need you to look for the Mailbag, I'm pretty", "sure it landed somewhere in Ponyville. Turn", "over the whole town if you have to.", "...we really can't be losing anymore mail..."), ("While you're at it see if you can deliver those", "letters you picked up earlier.", "", "...you can multitask right?")])
		elif self.trig == 2:
			if not self.dialogBox.visible:
				self.trig = 3
				self.mailAlert = cfg.objH.new(mailAlert, self.boxBrown, self.derpy, (68, -68))
				self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", [("Just look for ponies that are expecting mail", "and press "+cfg.keyH.keyCodeToString(cfg.oneButton).upper()+".", "", ""),])
		elif self.trig == 3:
			if not self.dialogBox.visible:
				if self.mailAlert is not None:
					self.mailAlert.destroy()
					self.mailAlert = None
					self.timer = 0
					self.trig = 4
		elif self.trig == 4:
			if self.timer < 7*60:
				self.derpy.set((self.derpy.body.position[0]+4, 300))
				self.boxBrown.set((self.boxBrown.body.position[0]+5, 250))
			else:
				self.finish()
				
		if self.bgPos[0] <= -4000+850:
			self.bgPos = (-4000+850, 0)
			self.bgStop = True
		
	def draw(self):
		for imgDef in self.bgImage:
			img = imgDef[0]
			ioW = imgDef[1]
			ioH = imgDef[2]
			position = ((self.bgPos[0]/3)+ioW, self.bgPos[1]+ioH)
			cfg.window.blit(img, position)
		for imgDef in self.bgImage2:
			img = imgDef[0]
			ioW = imgDef[1]
			ioH = imgDef[2]
			position = ((self.bgPos[0]+ioW, self.bgPos[1]+ioH))
			cfg.window.blit(img, position)

#intro cutscene controller
class introCutsceneController(base):
	
	def __init__(self):
		#base init
		base.__init__(self, (0, 0), None, False, True)
		cfg.keyH.assignKeyPress(cfg.startButton, self.finish)
		#dialog box
		self.dialogBox = None
		#
		self.part = 0
		self.bgImage = cfg.imgH.file["bg_cutscene_intro_treeHouse"][0]
		self.bgPos = (0, -675)
		self.timer = 0
		self.trig = 0
		self.depth = 900
		#box horse actor
		self.boxHorse = cfg.objH.new(actor, (-200, 400), "boxhorse_fly_r")
		self.boxHorse.imageSpeed = .2
		self.boxHorse.step = self.boxHorseSwagger
		self.boxHorse.dir = 0
		self.boxHorse.tighten = 0
		self.boxHorse.scale = 2
		#mailbag actor
		self.mailBag = cfg.objH.new(actor, (-200, 400), "env_mailbag_hanging_r")
		#bubble actors
		self.bOne = cfg.objH.new(actor, (-200, 400), "env_bubble")
		self.bOne.scale = 1.3
		self.bOne.alpha = 200
		self.bTwo = cfg.objH.new(actor, (-200, 400), "env_bubble")
		self.bTwo.scale = .7
		self.bTwo.alpha = 200
		self.bThree = cfg.objH.new(actor, (-200, 400), "env_bubble")
		self.bThree.alpha = 200
		#deryp actor
		self.derpy = cfg.objH.new(actor, (-200, 400), "derpy_intro_blowbubble")
		#bgoverlay
		self.bgOverlay = cfg.objH.new(actor, (0, 0), "bg_cutscene_intro_porch_overlay")
		self.bgOverlay.visible = False
		self.bgOverlay.depth = -900
		#door
		self.door = cfg.objH.new(actor, (0, 0), "env_cutscene_intro_door_closed")
		self.door.visible = False
		self.door.depth = -100
		#mail
		self.mailOne = cfg.objH.new(actor, (0, 0), "env_mail")
		self.mailTwo = cfg.objH.new(actor, (0, 0), "env_mail")
		self.mailThree = cfg.objH.new(actor, (0, 0), "env_mail")
		self.mailFour = cfg.objH.new(actor, (0, 0), "env_mail")
		self.mailFive = cfg.objH.new(actor, (0, 0), "env_mail")
		self.mailOne.visible = False
		self.mailTwo.visible = False
		self.mailThree.visible = False
		self.mailFour.visible = False
		self.mailFive.visible = False
		self.mailOne.scale = 1.1
		self.mailTwo.scale = 1
		self.mailThree.scale = .9
		self.mailFour.scale = .8
		self.mailFive.scale = 1.2
		self.mailOne.body.angle = .5
		self.mailTwo.body.angle = .5
		self.mailThree.body.angle = 1.2
		self.mailFour.body.angle = 2.8
		self.mailFive.body.angle = 3.3
		#music
		cfg.sndH.loop("music_intro")
		
	def finish(self):
		cfg.keyH.assignKeyPress(cfg.startButton, None)
		cfg.rmH.clearRoom()
		cfg.rmH.stageIntro("1", "Derpy's Treehouse", ("Collect 3 Letters",), cfg.rmH.stageOne)
		
	def step(self):
		#box pony flying to derpy's house
		if self.part == 0:
			if cfg.objH.frameSpeed == 1:
				self.timer += 2
			else:
				self.timer += 1
			if self.trig == 0 and self.timer >= 180:
				self.trig = 1
				self.timer = 0
			elif self.trig == 1:
				if self.timer >= 675:
					self.trig = 2
					self.timer = 0
					self.boxHorse.step = self.boxHorseFloat
				else:
					if cfg.objH.frameSpeed == 1:
						self.bgPos = (0, self.bgPos[1]+2)
					else:
						self.bgPos = (0, self.bgPos[1]+1)
			elif self.trig == 2:
				if self.timer >= 80:
					self.trig = 3
					self.timer = 0
					self.bgImage = cfg.imgH.file["bg_cutscene_intro_insideTreeHouse"][0]
					self.bgPos = (0, 0)
					self.boxHorse.set((-500, -500))
					self.boxHorse.step = self.asPass
					self.mailBag.set((-500, -500))
					self.bOne.set((250, 600))
					self.bTwo.set((500, 600))
					self.bThree.set((670, 600))
				else:
					pass
			elif self.trig == 3:
				if self.timer >= 300:
					self.trig = 4
					self.timer = 0
				else:
					self.bOne.impulse((4, -90))
					self.bTwo.impulse((2, -110))
					self.bThree.impulse((-3, -100))
					if self.bOne.body.position[1] < 200 and self.bOne.visible:
						if self.bOne.scale < 0.01:
							cfg.sndH.play("env_bubblepop")
							self.bOne.visible = False
						else:
							if cfg.objH.frameSpeed == 1:
								self.bOne.scale = self.bOne.scale/4
							else:
								self.bOne.scale = self.bOne.scale/2
					if self.bTwo.body.position[1] < 200 and self.bTwo.visible:
						if self.bTwo.scale < 0.01:
							cfg.sndH.play("env_bubblepop")
							self.bTwo.visible = False
						else:
							if cfg.objH.frameSpeed == 1:
								self.bTwo.scale = self.bTwo.scale/4
							else:
								self.bTwo.scale = self.bTwo.scale/2
					if self.bThree.body.position[1] < 200 and self.bThree.visible:
						if self.bThree.scale < 0.01:
							cfg.sndH.play("env_bubblepop")
							self.bThree.visible = False
						else:
							if cfg.objH.frameSpeed == 1:
								self.bThree.scale = self.bThree.scale/4
							else:
								self.bThree.scale = self.bThree.scale/2
			elif self.trig == 4:
				if self.timer >= 40:
					self.trig = 5
					self.timer = 0
				else:
					if cfg.objH.frameSpeed == 1:
						self.bgPos = (0, self.bgPos[1]-20)
						self.derpy.set((500, 720+self.bgPos[1]))
					else:
						self.bgPos = (0, self.bgPos[1]-10)
						self.derpy.set((500, 720+self.bgPos[1]))
					cfg.sndH.play("env_knock")
			elif self.trig == 5:
				if self.timer >= 45:
					self.trig = 6
					self.timer = 0
					self.derpy.set((500, 330))
				else:
					self.derpy.set((500, 330))
			elif self.trig == 6:
				if self.timer >= 15:
					self.trig = 7
					self.timer = 0
					cfg.sndH.play("effects_bwoing")
					self.derpy.setImage("derpy_cutscene_intro_blowbubble_openeyes")
				else:
					self.derpy.set((500, 330))
			elif self.trig == 7:
				if self.timer >= 45:
					self.trig = 8
					self.timer = 0
					self.bgPos = (0, 0)
					self.bgImage = cfg.imgH.file["bg_cutscene_intro_porch"][0]
					self.bgOverlay.visible = True
					self.derpy.visible = False
					self.door.visible = True
					self.door.set((254, 329))
					self.boxHorse.visible = True
					self.boxHorse.setImage("boxhorse_wait")
					self.boxHorse.scale = 1.5
					self.boxHorse.set((360, 350))
					self.boxHorse.imageSpeed = .05
					self.mailBag.visible = True
					self.mailBag.setImage("env_mailbag_laying_l")
					self.mailBag.scale = 1.5
					self.mailBag.set((360, 425))
				else:
					self.derpy.set((500, 330))
			elif self.trig == 8:
				if self.timer >= 300:
					self.trig = 9
					self.timer = 0
					self.door.setImage("env_cutscene_intro_door_open")
					self.mailBag.impulse((6000, -13000))
					cfg.sndH.play("effects_beooo")
					cfg.sndH.play("effects_clonk")
					self.door.set((254, 329))
					self.boxHorse.set((360, 350))
					self.boxHorse.setImage("boxhorse_hit")
					self.mailOne.visible = True
					self.mailTwo.visible = True
					self.mailThree.visible = True
					self.mailFour.visible = True
					self.mailFive.visible = True
					self.mailOne.set((360, 425))
					self.mailTwo.set((360, 425))
					self.mailThree.set((360, 425))
					self.mailFour.set((360, 425))
					self.mailFive.set((360, 425))
					self.mailOne.impulse((6000, -10000))
					self.mailTwo.impulse((8000, -5000))
					self.mailThree.impulse((7000, -7000))
					self.mailFour.impulse((10000, -2000))
					self.mailFive.impulse((3000, -18000))
					self.derpy.visible = True
					self.derpy.setImage("derpy_cutscene_intro_opendoor")
					self.derpy.scale = 2
					self.derpy.depth = -400
				else:
					self.door.set((254, 329))
					self.boxHorse.set((360, 350))
					self.mailBag.set((360, 425))
			elif self.trig == 9:
				if self.timer >= 90:
					self.trig = 10
					self.timer = 0
					self.derpy.setImage("derpy_walk_r")
					self.derpy.imageSpeed = .25
					self.derpy.set((140, 370))
					self.door.set((254, 329))
				else:
					self.door.set((254, 329))
					self.boxHorse.set((360, 330))
					self.derpy.set((140, 370))
					if self.mailBag.scale > 1:
						self.mailBag.scale -= .05
					elif self.mailBag.scale > .5:
						self.mailBag.scale -= .01
					else:
						self.derpy.setImage("derpy_cutscene_intro_opendoor_openeyes")
			elif self.trig == 10:
				if self.timer >= 170:
					self.trig = 11
					self.timer = 0
					self.door.set((254, 329))
					self.derpy.set((376, 378))
					self.derpy.setImage("derpy_stand_r")
					self.door.setImage("env_cutscene_intro_door_closed")
					cfg.sndH.play("effects_clonk")
				else:
					self.door.set((254, 329))
					self.boxHorse.set((360, 330))
					if cfg.objH.frameSpeed == 1:
						self.derpy.set((self.derpy.body.position[0]+2.8, 370))
					else:
						self.derpy.set((self.derpy.body.position[0]+1.4, 370))
			elif self.trig == 11:
				if self.timer >= 90:
					self.trig = 12
					self.timer = 0
					self.boxHorse.setImage("boxhorse_mad_l")
				else:
					self.door.set((254, 329))
					self.derpy.set((376, 378))
					self.boxHorse.set((360, 330))
			elif self.trig == 12:
				if self.timer >= 60:
					self.trig = 13
					self.timer = 0
					self.boxHorse.setImage("boxhorse_mad_r")
					self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", (('*grumble*', '...', 'Good...morning Derpy.', ''),("You'd better get that mail you scattered",'before the wind picks it up.','...','................Stupid backwards doors.')))
				else:
					self.door.set((254, 329))
					self.derpy.set((376, 378))
					self.boxHorse.set((360, 330))
			elif self.trig == 13:
				if not self.dialogBox.visible:
					self.trig = 14
					self.timer = 0
					self.dialogBox.destroy()
					self.door.set((254, 329))
					self.derpy.set((376, 338))
					self.boxHorse.set((360, 330))
					self.derpy.setImage("derpy_fly_r")
				else:
					self.door.set((254, 329))
					self.derpy.set((376, 378))
					self.boxHorse.set((360, 330))
			elif self.trig == 14:
				if self.timer >= 110:
					self.trig = 15
					self.timer = 0
					self.dialogBox = cfg.objH.new(dialog, "boxhorse_talkinghead", (('Bring all the letters you can find back to','me up here.',"I'm sure they couldn't have gone too far.",''),('You remember how to pick things up right?', '....................................?', '...Just.......use '+cfg.keyH.keyCodeToString(cfg.twoButton).upper()+', okay?', '')))
				else:
					self.door.set((254, 329))
					self.boxHorse.set((360, 330))
					self.derpy.impulse((0, -100))
			elif self.trig == 15:
				if not self.dialogBox.visible:
					self.trig = 16
					self.timer = 0
					self.dialogBox.destroy()
					self.door.set((254, 329))
					self.derpy.set((376, 200))
				else:
					self.boxHorse.set((360, 330))
					self.door.set((254, 329))
					self.boxHorse.set((360, 330))
					self.derpy.set((376, 200))
			elif self.trig == 16:
				if self.timer >= 240:
					self.finish()
				else:
					self.boxHorse.set((360, 330))
					self.door.set((254, 329))
					self.derpy.impulse((50, -70))
					self.derpy.depth = -9999
		self.bgOverlay.body.position = (self.bgPos[0]+(420), self.bgPos[1]+(263))
				
	def boxHorseSwagger(self):
		if self.boxHorse.scale > 1:
			if cfg.objH.frameSpeed == 1:
				self.boxHorse.scale -= .003
			else:
				self.boxHorse.scale -= .0015
		elif self.boxHorse.scale < 1:
			self.boxHorse.scale = 1
		self.mailBag.scale = self.boxHorse.scale
		if self.boxHorse.dir == 0:
			self.boxHorse.impulse((100, -55))
			self.mailBag.set((self.boxHorse.body.position[0]+int(45*self.boxHorse.scale), self.boxHorse.body.position[1]+int(5*self.boxHorse.scale)))
			self.mailBag.depth = 100
		else:
			self.boxHorse.impulse((-100, -55))
			self.mailBag.set((self.boxHorse.body.position[0]-int(45*self.boxHorse.scale), self.boxHorse.body.position[1]+int(5*self.boxHorse.scale)))
			self.mailBag.depth = -100
		if self.boxHorse.body.position[0]-self.boxHorse.tighten < 150 and self.boxHorse.dir == 1:
			self.boxHorse.dir = 0
			self.boxHorse.tighten += 20
			self.boxHorse.setImage("boxhorse_fly_r")
			self.mailBag.setImage("env_mailbag_hanging_r")
		elif self.boxHorse.body.position[0]+self.boxHorse.tighten > 550 and self.boxHorse.dir == 0:
			self.boxHorse.dir = 1
			self.boxHorse.tighten += 20
			self.boxHorse.setImage("boxhorse_fly_l")
			self.mailBag.setImage("env_mailbag_hanging_l")
	
	def boxHorseFloat(self):
		self.mailBag.set((self.boxHorse.body.position[0]-45, self.boxHorse.body.position[1]+5))
		self.boxHorse.impulse((10, -40))
		self.boxHorse.setImage("boxhorse_fly_l")
	
	def asPass(self):
		pass
		
				
	def draw(self):
		for imgDef in self.bgImage:
			img = imgDef[0]
			ioW = imgDef[1]
			ioH = imgDef[2]
			position = (self.bgPos[0]+ioW, self.bgPos[1]+ioH)
			cfg.window.blit(img, position)
		#cfg.window.blit(self.bgImage, self.bgPos)
		