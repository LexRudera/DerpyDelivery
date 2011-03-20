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
import pygame


#handles object
class mainMenuController(base):
	
	def __init__(self):
		#base init
		base.__init__(self, (0, 0), None)
		cfg.keyH.assignKeyPress(cfg.startButton, self.startGame)
		cfg.keyH.assignKeyPress(pygame.K_t, self.skip)
		self.text = cfg.objH.largeText.render('<Press '+cfg.keyH.keyCodeToString(cfg.startButton).upper()+' To Start>', 0, (224, 47, 47))
		self.text.set_alpha(255)
		self.fade = 5

	def draw(self):
		self.text.set_alpha(self.text.get_alpha()-self.fade)
		if self.text.get_alpha() <= 170:
			self.fade = -5
		elif self.text.get_alpha() >= 255:
			self.fade = 5
		cfg.window.blit(self.text, (420-(self.text.get_width()/2),450))
		
	def destroy(self):
		base.destroy(self)
		cfg.keyH.assignKeyDown(pygame.K_SPACE, None)
		
	def startGame(self):
		cfg.rmH.clearRoom()
		cfg.rmH.introCutscene()
		
	def skip(self):
		cfg.objH.stageScores["1"] = [("TIME", "0"), ("TOTAL", "0")]
		cfg.rmH.clearRoom()
		cfg.rmH.stageTwoCutscene()
		
class endStage(base):
	def __init__(self, number, bonuses, targetRoom):
		#base init
		base.__init__(self, (0, 0), None)
		cfg.keyH.assignKeyPress(cfg.startButton, self.nextRoom)
		self.contText = cfg.objH.largeText.render('<Press '+cfg.keyH.keyCodeToString(cfg.startButton).upper()+' To Continue>', 0, (255, 255, 255))
		self.stageNumber = cfg.objH.veryLargeText.render('Stage '+number+' Complete!', 0, (255, 255, 255))
		self.bonuses = []
		for bonus in bonuses:
			color = (255, 255, 255)
			if len(bonus) == 3:
				color = (236, 196, 188)
			obj = cfg.objH.largeText.render(bonus[0]+':', 0, color)
			val = cfg.objH.largeText.render(bonus[1], 0, color)
			self.bonuses.append((obj, val, 0))
		self.stageNumberPos = -900
		self.phase = 0
		self.targetRoom = targetRoom
		cfg.objH.stageScores[number] = bonuses
	
	def nextRoom(self):
		cfg.keyH.assignKeyDown(pygame.K_SPACE, None)
		cfg.rmH.clearRoom()
		self.targetRoom()
		
	def draw(self):
		if self.phase == 0:
			if cfg.objH.frameSpeed == 1:
				self.stageNumberPos += 40
			else:
				self.stageNumberPos += 20
			if self.stageNumberPos >= 50:
				self.stageNumberPos = 50
				self.phase = 1
		elif self.phase == 1:
			for i, bonus in enumerate(self.bonuses):
				if bonus[2] >= 255:
					self.bonuses[i] = (bonus[0], bonus[1], 255)
				else:
					if cfg.objH.frameSpeed == 1:
						self.bonuses[i] = (bonus[0], bonus[1], bonus[2] + 45)
					else:
						self.bonuses[i] = (bonus[0], bonus[1], bonus[2] + 30)
					break
		tBonus = []
		for bonus in self.bonuses:
			obj = bonus[0]
			obj.set_alpha(bonus[2])
			val = bonus[1]
			val.set_alpha(bonus[2])
			tBonus.append((obj, val))
		cfg.window.blit(self.stageNumber, (self.stageNumberPos, 30))
		for i, bonus in enumerate(tBonus):
			if i == len(tBonus)-1:
				i+=1
			cfg.window.blit(bonus[0], (480-bonus[0].get_width(), 160+(i*25)))
			cfg.window.blit(bonus[1], (550, 160+(i*25)))
		cfg.window.blit(self.contText, (420-(self.contText.get_width()/2), 500))
		
		
class startStage(base):
	
	def __init__(self, number, name, objective, targetRoom):
		#base init
		base.__init__(self, (0, 0), None)
		cfg.keyH.assignKeyPress(cfg.startButton, self.startStage)
		self.startText = cfg.objH.largeText.render('<Press '+cfg.keyH.keyCodeToString(cfg.startButton).upper()+' To Start>', 0, (255, 255, 255))
		self.stageNumber = cfg.objH.veryLargeText.render('Stage '+number+':', 0, (255, 255, 255))
		self.stageName = cfg.objH.veryLargeText.render(name, 0, (255, 255, 255))
		self.stageObjectives = []
		for obj in objective:
			self.stageObjectives.append(cfg.objH.largeText.render('- '+obj+' -', 0, (255, 255, 255)))
		self.targetRoom = targetRoom
		self.stageNumberPos = -900
		self.stageNamePos = 900
		self.objectiveAlpha = 0
		self.phase = 0
		
	def startStage(self):
		cfg.keyH.assignKeyDown(pygame.K_SPACE, None)
		cfg.rmH.clearRoom()
		self.targetRoom()
		
	def draw(self):
		if self.phase == 0:
			if cfg.objH.frameSpeed == 1:
				self.stageNumberPos += 40
			else:
				self.stageNumberPos += 20
			if self.stageNumberPos >= 50:
				self.stageNumberPos = 50
				self.phase = 1
		elif self.phase == 1:
			if cfg.objH.frameSpeed == 1:
				self.stageNamePos -= 40
			else:
				self.stageNamePos -= 20
			if self.stageNamePos <= 150:
				self.stageNamePos = 150
				self.phase = 2
		elif self.phase == 2:
			if cfg.objH.frameSpeed == 1:
				self.objectiveAlpha += 60
			else:
				self.objectiveAlpha += 30
			if self.objectiveAlpha >= 255:
				self.objectiveAlpha = 255
				self.phase = 3
		cfg.window.blit(self.stageNumber, (self.stageNumberPos, 30))
		cfg.window.blit(self.stageName, (self.stageNamePos, 100))
		for i, objective in enumerate(self.stageObjectives):
			objective.set_alpha(self.objectiveAlpha)
			cfg.window.blit(objective, (420-(objective.get_width()/2), 300+(i*35)))
		cfg.window.blit(self.startText, (420-(self.startText.get_width()/2), 500))
		
class optionsMenu(base):

	def __init__(self):
		#base init
		base.__init__(self, (0, 0), None)
		self.depth = -999
		self.blackSurface = pygame.Surface((840, 525))
		self.blackSurface = self.blackSurface.convert(cfg.window)
		self.blackSurface.fill((0,0,0))
		self.blackSurface.set_alpha(200)
		self.pauseText = cfg.objH.largeText.render('Options:', 0, (237, 203, 13))
		self.soundText = cfg.objH.largeText.render('Preferences', 0, (237, 203, 13))
		self.controlsText = cfg.objH.largeText.render('Controls', 0, (237, 203, 13))
		self.saveText = cfg.objH.largeText.render('Save Settings', 0, (237, 203, 13))
		self.restartText = cfg.objH.largeText.render('Restart Level', 0, (237, 203, 13))
		if cfg.rmH.currentRoom == cfg.rmH.mainMenu:
			self.restartText.set_alpha(50)
			self.quitText = cfg.objH.largeText.render('Quit Game', 0, (237, 203, 13))
		else:
			self.quitText = cfg.objH.largeText.render('Main Menu', 0, (237, 203, 13))
		self.soundMusicVol = cfg.objH.mediumText.render('Music Volume: ', 0, (237, 203, 13))
		self.soundEffectVol = cfg.objH.mediumText.render('Effect Volume: ', 0, (237, 203, 13))
		self.arrowText = cfg.objH.largeText.render('>', 0, (237, 203, 13))
		self.menuPos = 0
		self.subMenuPos = 0
		self.djpon3x = 0
		self.subMenu = None
		self.roomLoopMusic = cfg.sndH.currentLoop
		cfg.keyH.assignKeyPress(cfg.upButton, self.menuUp)
		cfg.keyH.assignKeyPress(cfg.downButton, self.menuDown)
		cfg.keyH.assignKeyPress(cfg.twoButton, self.menuSelect)
		cfg.keyH.assignKeyPress(cfg.oneButton, self.menuBack)
		self.modKeyList = []
		self.modifyingKey = False
		
	def menuUp(self):
		if not self.modifyingKey:
			cfg.sndH.play("temp_weor")
			if self.subMenu is None:
				if self.menuPos > 0:
					self.menuPos -= 1
				else:
					self.menuPos = 4
			elif self.subMenu == 0:
				if self.subMenuPos > 0:
					self.subMenuPos -= 1
				else:
					self.subMenuPos = 1
			elif self.subMenu == 1:
				if self.subMenuPos > 0:
					self.subMenuPos -= 1
				else:
					self.subMenuPos = 8
	
	def menuDown(self):
		if not self.modifyingKey:
			cfg.sndH.play("temp_weor")
			if self.subMenu is None:
				if self.menuPos < 4:
					self.menuPos += 1
				else:
					self.menuPos = 0
			elif self.subMenu == 0:
				if self.subMenuPos < 1:
					self.subMenuPos += 1
				else:
					self.subMenuPos = 0
			elif self.subMenu == 1:
				if self.subMenuPos < 8:
					self.subMenuPos += 1
				else:
					self.subMenuPos = 0
	
	def modKey(self):
		for r in cfg.keyH.down:
			if r not in self.modKeyList:
				if r != cfg.rightButton and r != cfg.upButton and r != cfg.leftButton and r != cfg.downButton and r != cfg.oneButton and r != cfg.twoButton and r != cfg.startButton and r != cfg.menuButton:
					self.modifyingKey = False
					self.modKeyList = []
					preKeyReleaseEvent = None
					preKeyPressEvent = None
					preKeyDownEvent = None
					keyReleaseEvent = None
					keyPressEvent = None
					keyDownEvent = None
					keyToMod = None
					
					if self.subMenuPos == 0:
						keyToMod = cfg.rightButton
					elif self.subMenuPos == 1:
						keyToMod = cfg.upButton
					elif self.subMenuPos == 2:
						keyToMod = cfg.leftButton
					elif self.subMenuPos == 3:
						keyToMod = cfg.downButton
					elif self.subMenuPos == 4:
						keyToMod = cfg.oneButton
					elif self.subMenuPos == 5:
						keyToMod = cfg.twoButton
					elif self.subMenuPos == 6:
						keyToMod = cfg.startButton
					elif self.subMenuPos == 7:
						keyToMod = cfg.menuButton
					
					keyToMod = str(keyToMod)
						
					if keyToMod in cfg.keyH.keyRelease:
						keyReleaseEvent = cfg.keyH.keyRelease[keyToMod]
						cfg.keyH.assignKeyRelease(keyToMod, None)
					if keyToMod in cfg.objH.keyReleasedPrePause:
						preKeyReleaseEvent = cfg.objH.keyReleasedPrePause[keyToMod]
						del cfg.objH.keyReleasedPrePause[keyToMod]
						
					if keyToMod in cfg.keyH.keyPress:
						keyPressEvent = cfg.keyH.keyPress[keyToMod]
						cfg.keyH.assignKeyPress(keyToMod, None)
					if keyToMod in cfg.objH.keyPressPrePause:
						preKeyPressEvent = cfg.objH.keyPressPrePause[keyToMod]
						del cfg.objH.keyPressPrePause[keyToMod]
						
					if keyToMod in cfg.keyH.keyDown:
						keyDownEvent = cfg.keyH.keyDown[keyToMod]
						cfg.keyH.assignKeyPress(keyToMod, None)
					if keyToMod in cfg.objH.keyDownPrePause:
						preKeyDownEvent = cfg.objH.keyDownPrePause[keyToMod]
						del cfg.objH.keyDownPrePause[keyToMod]
					
					if self.subMenuPos == 0:
						cfg.rightButton = r
					elif self.subMenuPos == 1:
						cfg.upButton = r
					elif self.subMenuPos == 2:
						cfg.leftButton = r
					elif self.subMenuPos == 3:
						cfg.downButton = r
					elif self.subMenuPos == 4:
						cfg.oneButton = r
					elif self.subMenuPos == 5:
						cfg.twoButton = r
					elif self.subMenuPos == 6:
						cfg.startButton = r
					elif self.subMenuPos == 7:
						cfg.menuButton = r
					
					cfg.keyH.assignKeyRelease(r, keyReleaseEvent)
					cfg.keyH.assignKeyPress(r, keyPressEvent)
					cfg.keyH.assignKeyDown(r, keyDownEvent)
					
					if preKeyReleaseEvent is not None:
						cfg.objH.keyReleasedPrePause[r] = preKeyReleaseEvent
					if preKeyPressEvent is not None:
						cfg.objH.keyPressPrePause[r] = preKeyPressEvent
					if preKeyDownEvent is not None:
						cfg.objH.keyDownPrePause[r] = preKeyDownEvent
					
					cfg.sndH.play("effects_sparkle")
				else:
					cfg.sndH.play("effects_clonk")
					
	def menuSelect(self):
		if self.subMenu is None:
			if self.menuPos == 0:
				self.subMenu = 0
				self.subMenuPos = 0
			elif self.menuPos == 1:
				self.subMenu = 1
				self.subMenuPos = 0
			elif self.menuPos == 2:
				cfg.objH.saveSettings()
			elif self.menuPos == 3:
				if cfg.rmH.currentRoom != cfg.rmH.mainMenu:
					cfg.rmH.pause()
					cfg.rmH.clearRoom()
					cfg.rmH.currentRoom()
			elif self.menuPos == 4:
				if cfg.rmH.currentRoom != cfg.rmH.mainMenu:
					cfg.rmH.pause()
					cfg.rmH.clearRoom()
					cfg.rmH.mainMenu()
				else:
					pygame.event.post(pygame.event.Event(pygame.QUIT))
		elif self.subMenu == 0:
			if self.subMenuPos == 0:
				cfg.sndH.musicVolume -= .1
				if cfg.sndH.musicVolume <= 0:
					cfg.sndH.musicVolume = 1
			elif self.subMenuPos == 1:
				cfg.sndH.effectVolume -= .1
				if cfg.sndH.effectVolume <= 0:
					cfg.sndH.effectVolume = 1
			elif self.subMenuPos == 2:
				if cfg.objH.frameSpeed == 2:
					cfg.objH.frameSpeed = 1
				else:
					cfg.objH.frameSpeed = 2
			cfg.sndH.file["music_djpon3"].set_volume(cfg.sndH.musicVolume)
		elif self.subMenu == 1 and not self.modifyingKey:
			if self.subMenuPos == 8:
				cfg.keyH.getJoysticks()
			else:
				self.modifyingKey = True
				self.modKeyList = cfg.keyH.down.copy()
		if not self.modifyingKey:
			cfg.sndH.play("temp_weor")
	
	def menuBack(self):
		if not self.modifyingKey:
			if self.subMenu is None:
				cfg.rmH.pause()
			else:
				self.subMenu = None
			
	def draw(self):
		if self.modifyingKey:
			self.modKey()
		cfg.window.blit(self.blackSurface, (0,0))
		cfg.window.blit(self.pauseText, (320, 100))
		cfg.window.blit(self.soundText, (100, 250))
		cfg.window.blit(self.controlsText, (100, 300))
		cfg.window.blit(self.saveText, (100, 350))
		cfg.window.blit(self.restartText, (100, 400))
		cfg.window.blit(self.quitText, (100, 450))
		if self.subMenu == 0:
			if cfg.sndH.currentLoop != "music_djpon3":
				cfg.sndH.loop("music_djpon3")
			if self.djpon3x < 280:
				if cfg.objH.frameSpeed == 1:
					self.djpon3x += 20
				else:
					self.djpon3x += 10
			musicVolumeText = cfg.objH.mediumText.render(str(int(cfg.sndH.musicVolume*100))+'%', 0, (237, 203, 13))
			effectVolumeText = cfg.objH.mediumText.render(str(int(cfg.sndH.effectVolume*100))+'%', 0, (237, 203, 13))
			cfg.window.blit(self.soundMusicVol, (450, 300))
			cfg.window.blit(musicVolumeText, (650, 300))
			cfg.window.blit(self.soundEffectVol, (450, 350))
			cfg.window.blit(effectVolumeText, (650, 350))
			cfg.window.blit(self.arrowText, (420, 295+(self.subMenuPos*50)))
			for d in cfg.imgH.file["djpon3_optionsMenu"][0]:
				cfg.window.blit(d[0], (840-self.djpon3x+d[1], 260+d[2]))
		elif self.subMenu == 1:
			peripheralsText = None
			peripheralText = []
			if cfg.keyH.joysticks != []:
				peripheralsText = cfg.objH.mediumText.render('Detected Peripherals:', 0, (237, 203, 13))
				for j in cfg.keyH.joysticks:
					peripheralText.append(cfg.objH.smallText.render(j.get_name(), 0, (237, 203, 13)))
			else:
				peripheralsText = cfg.objH.mediumText.render('No Peripherals Detected.', 0, (237, 203, 13))
			
			rightText = cfg.objH.smallText.render('Right: '+cfg.keyH.keyCodeToString(cfg.rightButton).upper(), 0, (237, 203, 13))
			upText = cfg.objH.smallText.render('Up:    '+cfg.keyH.keyCodeToString(cfg.upButton).upper(), 0, (237, 203, 13))
			leftText = cfg.objH.smallText.render('Left:  '+cfg.keyH.keyCodeToString(cfg.leftButton).upper(), 0, (237, 203, 13))
			downText = cfg.objH.smallText.render('Down:  '+cfg.keyH.keyCodeToString(cfg.downButton).upper(), 0, (237, 203, 13))
			oneText = cfg.objH.smallText.render('1:     '+cfg.keyH.keyCodeToString(cfg.oneButton).upper(), 0, (237, 203, 13))
			twoText = cfg.objH.smallText.render('2:     '+cfg.keyH.keyCodeToString(cfg.twoButton).upper(), 0, (237, 203, 13))
			startText = cfg.objH.smallText.render('Start: '+cfg.keyH.keyCodeToString(cfg.startButton).upper(), 0, (237, 203, 13))
			menuText = cfg.objH.smallText.render('Menu:  '+cfg.keyH.keyCodeToString(cfg.menuButton).upper(), 0, (237, 203, 13))
			detectText = cfg.objH.smallText.render('Detect Peripherals', 0, (237, 203, 13))
			if self.modifyingKey:
				backing = pygame.Surface((500, 10))
				backing.fill((255, 0, 0))
				backing.set_alpha(128)
				cfg.window.blit(backing, (450, 300+(self.subMenuPos*20)))
			cfg.window.blit(rightText, (450, 300))
			cfg.window.blit(upText, (450, 320))
			cfg.window.blit(leftText, (450, 340))
			cfg.window.blit(downText, (450, 360))
			cfg.window.blit(oneText, (450, 380))
			cfg.window.blit(twoText, (450, 400))
			cfg.window.blit(startText, (450, 420))
			cfg.window.blit(menuText, (450, 440))
			cfg.window.blit(detectText, (450, 460))
			cfg.window.blit(self.arrowText, (420, 295+(self.subMenuPos*20)))
			cfg.window.blit(peripheralsText, (450, 170))
			for i, p in enumerate(peripheralText):
				cfg.window.blit(p, (450, 190+(i*15)))
		else:
			cfg.window.blit(self.arrowText, (70, 250+(self.menuPos*50)))
			self.djpon3x = 0
			if cfg.sndH.currentLoop != self.roomLoopMusic and self.roomLoopMusic is not None:
				cfg.sndH.loop(self.roomLoopMusic)
		