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

#64x64 crate
class crate(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_crate", True, False)
		self.body.mass = 2
		#shape
		self.stuffs = self.addRect((0, 0), (64, 64))

#balloon
class balloon(base):

	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_balloon")
		self.body.mass = 1
		#shape
		self.addCircle(32)
		self.drawffset = (0, 32)
		
	def step(self):
		self.impulse((0, -10))