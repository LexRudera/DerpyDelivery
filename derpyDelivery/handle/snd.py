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
import os
import pygame
from derpyDelivery import cfg

#handles sounds
class handler():
	
	def __init__(self):
		self.file = {}
		self.channels = {}
		pygame.mixer.set_num_channels(0)
		#generate the sounds to search for from files in the img folder
		for dirTree in os.walk(os.path.abspath("snd")):
			for file in dirTree[2]:
				path = str(dirTree[0])
				path = path.replace(os.path.abspath("snd"), "")[1:]
				path = path.replace("/", "_")
				path = path.replace("\\", "_")
				path = path + "_" + file.replace(".ogg", "")
				self.file[path] = None
	#attempts to load a single sound in the file definitions
	#returns the name of the loaded file if successful
	#returns None if no file was loaded
	def load(self):
		#loop through all the file place holders until we find one that has not been loaded
		for files in self.file:
			if self.file[files] is None:
				#construct the file path from the dictionary key
				filePath = ""
				for piece in files.split("_"):
					filePath = os.path.join(filePath, piece)
				#create the sound
				filePath = os.path.join(os.path.abspath("snd"), filePath)
				if os.path.exists(filePath + ".ogg"):
					self.file[files] = self.__loadSound(filePath + ".ogg")		#load
					pygame.mixer.set_num_channels(pygame.mixer.get_num_channels()+1)
					self.channels[files] = pygame.mixer.Channel(pygame.mixer.get_num_channels()-1)
				return files
		return None
	
	#loads a sound
	def __loadSound(self, filePath):
		sound = pygame.mixer.Sound(filePath)
		return sound
		
	#play sound
	def play(self, soundIndex):
		self.channels[soundIndex].stop()
		self.channels[soundIndex].play(self.file[soundIndex])
		
	#loop sound
	def loop(self, soundIndex):
		self.channels[soundIndex].stop()
		self.channels[soundIndex].play(self.file[soundIndex], -1)
		
	#stop sound
	def stop(self, soundIndex):
		self.channels[soundIndex].stop()
		
		