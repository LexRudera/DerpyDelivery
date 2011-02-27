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

#handles objects
class handler():
	
	def __init__(self):
		self.bgImage = None
		self.bgRepeat = (False, False)
		self.dimensions = (0, 0)
		
	def clearRoom(self):
		for instance in base.instances:
			instance.destroy()
			
	def mainMenu(self):
		self.bgImage = cfg.imgH.file["bg_menu"][0]
		self.bgRepeat = (True, True)
		self.dimensions = (840, 525)
		cfg.objH.new(objects.mainMenuController)
		
	def testRoom(self):
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