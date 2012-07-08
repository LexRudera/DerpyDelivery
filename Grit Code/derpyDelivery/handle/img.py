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
from math import ceil
import pygame.rect
import pygame.surface

#handles images
class handler():
	
	def __init__(self):
		self.file = {}
		#generate the images to search for from files in the img folder
		for dirTree in os.walk(os.path.join(cfg.root_path, "img")):
			for file in dirTree[2]:
				path = str(dirTree[0])
				path = path.replace(os.path.join(cfg.root_path, "img"), "")[1:]
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
				filePath = os.path.join(os.path.join(cfg.root_path, "img"), filePath)
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
		image = image.convert()
		image.set_colorkey((0,255,0))					#set transparency key to (0, 255, 0)
		clipW = 250
		clipH = 250
		if image.get_width() <= clipW and image.get_height() <= clipH:
			#return image
			return image
		else:
			images = []
			#shred image
			hT = int(ceil(image.get_width()/clipW))
			vT = int(ceil(image.get_height()/clipH))
			for hi in range(0, hT+1):
				dW = clipW
				if (hi+1)*clipW > image.get_width():
					dW = clipW-(((hi+1)*clipW)-image.get_width())
				for vi in range(0, vT+1):
					clipRect = pygame.rect.Rect((hi*clipW, vi*clipH), (clipW, clipH))
					dH = clipH
					if (vi+1)*clipH > image.get_height():
						dH = clipH-(((vi+1)*clipH)-image.get_height())
					clipImage = pygame.surface.Surface((dW, dH))
					clipImage = clipImage.convert()
					clipImage.fill((0,255,0))
					clipImage.set_colorkey((0,255,0))
					clipImage.blit(image, (0,0), clipRect)
					images.append((clipImage, hi*clipW, vi*clipH))
			return images