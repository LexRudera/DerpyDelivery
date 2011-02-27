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

#handles images
class handler():
	
	def __init__(self):
		self.file = {}
		#generate the images to search for from files in the img folder
		for dirTree in os.walk(os.path.abspath("img")):
			for file in dirTree[2]:
				path = str(dirTree[0])
				path = path.replace(os.path.abspath("img"), "")[1:]
				path = path.replace("/", "_")
				path = path.replace("\\", "_")
				self.file[path] = None
	
	#attempts to load a single image in the file definitions
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
				#create the sprite, load all the frames
				index = 0
				frames = []
				filePath = os.path.join(os.path.abspath("img"), filePath)
				while os.path.exists(os.path.join(filePath, str(index) + ".png")):
					frames.append(self.__loadImage(os.path.join(filePath, str(index) + ".png")))			#load
					index += 1
				#assign the frames to the file
				self.file[files] = frames
				return files
		return None
	
	#loads an image
	def __loadImage(self, filePath):
		image = pygame.image.load(filePath)								#load image
		image = image.convert(cfg.window)
		image.set_colorkey((0,255,0), pygame.HWSURFACE)					#set transparency key to (0, 255, 0)
		return image
		
		