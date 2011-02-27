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

import pygame

#handles keyboard input
class handler():
	
	def __init__(self):
		self.keyRelease = {}
		self.keyDown = {}
		self.keyPress = {}
		self.down = {}
		
	def assignKeyRelease(self, keyEvent, task):
		strKeyEvent = str(keyEvent)
		if task is not None:
			self.keyRelease[strKeyEvent] = task
		else:
			if strKeyEvent in self.keyRelease:
				del self.keyRelease[strKeyEvent]
		
	def assignKeyDown(self, keyEvent, task):
		strKeyEvent = str(keyEvent)
		if task is not None:
			self.keyDown[strKeyEvent] = task
		else:
			if strKeyEvent in self.keyDown:
				del self.keyDown[strKeyEvent]
		
	def assignKeyPress(self, keyEvent, task):
		strKeyEvent = str(keyEvent)
		if task is not None:
			self.keyPress[strKeyEvent] = task
		else:
			if strKeyEvent in self.keyPress:
				del self.keyPress[strKeyEvent]
	
	#process when a press happens
	def processPress(self, event):
		key = str(event.key)
		self.down[key] = True	#set the key to down
		if key in self.keyPress:
			self.keyPress[key]()
	
	#process when a release happens
	def processRelease(self, event):
		key = str(event.key)
		del self.down[key]		#remove the key from down position
		if key in self.keyRelease:
			self.keyRelease[key]()

	#processes all pressed keys
	def process(self):
		for key in self.down:
			if key in self.keyDown:
				self.keyDown[key]()
		
	
		