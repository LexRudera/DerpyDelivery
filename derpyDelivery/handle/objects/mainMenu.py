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
		cfg.keyH.assignKeyDown(pygame.K_SPACE, self.startGame)
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
		cfg.rmH.testRoom()