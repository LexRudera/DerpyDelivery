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
		cfg.keyH.assignKeyPress(pygame.K_SPACE, self.startGame)
		self.text = cfg.objH.largeText.render('<Press "Space" To Start>', 0, (224, 47, 47))
		self.text.set_alpha(255)
		self.fade = 5

	def draw(self):
		self.text.set_alpha(self.text.get_alpha()-self.fade)
		if self.text.get_alpha() <= 170:
			self.fade = -5
		elif self.text.get_alpha() >= 255:
			self.fade = 5
		cfg.window.blit(self.text, (150,450))
		
	def destroy(self):
		base.destroy(self)
		cfg.keyH.assignKeyDown(pygame.K_SPACE, None)
		
	def startGame(self):
		cfg.rmH.clearRoom()
		cfg.rmH.introCutscene()
		
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
		self.soundText = cfg.objH.largeText.render('Sounds', 0, (237, 203, 13))
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
		cfg.keyH.assignKeyPress(pygame.K_UP, self.menuUp)
		cfg.keyH.assignKeyPress(pygame.K_DOWN, self.menuDown)
		cfg.keyH.assignKeyPress(pygame.K_z, self.menuSelect)
		cfg.keyH.assignKeyPress(pygame.K_x, self.menuBack)
		
	def menuUp(self):
		cfg.sndH.play("temp_weor")
		if self.subMenu is None:
			if self.menuPos > 0:
				self.menuPos -= 1
			else:
				self.menuPos = 2
		elif self.subMenu == 0:
			if self.subMenuPos > 0:
				self.subMenuPos -= 1
			else:
				self.subMenuPos = 1
	
	def menuDown(self):
		cfg.sndH.play("temp_weor")
		if self.subMenu is None:
			if self.menuPos < 2:
				self.menuPos += 1
			else:
				self.menuPos = 0
		elif self.subMenu == 0:
			if self.subMenuPos < 1:
				self.subMenuPos += 1
			else:
				self.subMenuPos = 0
			
	def menuSelect(self):
		if self.subMenu is None:
			if self.menuPos == 0:
				self.subMenu = 0
			elif self.menuPos == 1:
				if cfg.rmH.currentRoom != cfg.rmH.mainMenu:
					cfg.rmH.pause()
					cfg.rmH.clearRoom()
					cfg.rmH.currentRoom()
			elif self.menuPos == 2:
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
			cfg.sndH.file["music_djpon3"].set_volume(cfg.sndH.musicVolume)
		cfg.sndH.play("temp_weor")
	
	def menuBack(self):
		if self.subMenu is None:
			cfg.rmH.pause()
		else:
			self.subMenu = None
			
	def draw(self):
		cfg.window.blit(self.blackSurface, (0,0))
		cfg.window.blit(self.pauseText, (320, 100))
		cfg.window.blit(self.soundText, (100, 300))
		cfg.window.blit(self.restartText, (100, 350))
		cfg.window.blit(self.quitText, (100, 400))
		if self.subMenu == 0:
			if cfg.sndH.currentLoop != "music_djpon3":
				cfg.sndH.loop("music_djpon3")
			if self.djpon3x < 280:
				self.djpon3x += 10
			musicVolumeText = cfg.objH.mediumText.render(str(int(cfg.sndH.musicVolume*100))+'%', 0, (237, 203, 13))
			effectVolumeText = cfg.objH.mediumText.render(str(int(cfg.sndH.effectVolume*100))+'%', 0, (237, 203, 13))
			cfg.window.blit(self.soundMusicVol, (450, 300))
			cfg.window.blit(musicVolumeText, (650, 300))
			cfg.window.blit(self.soundEffectVol, (450, 350))
			cfg.window.blit(effectVolumeText, (650, 350))
			cfg.window.blit(self.arrowText, (420, 295+(self.subMenuPos*50)))
			cfg.window.blit(cfg.imgH.file["djpon3_optionsMenu"][0], (840-self.djpon3x, 260))
		else:
			cfg.window.blit(self.arrowText, (70, 300+(self.menuPos*50)))
			self.djpon3x = 0
			if cfg.sndH.currentLoop != self.roomLoopMusic:
				cfg.sndH.loop(self.roomLoopMusic)
		