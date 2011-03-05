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

#handles object
class dynamicBlock(base):
	
	def __init__(self, position, dimensions):
		#base init
		base.__init__(self, (position[0]+dimensions[0]/2, position[1]+dimensions[1]/2), None, True, True)
		#shape
		self.addRect((0,0), dimensions)
		
class dynamicPoly(base):
	def __init__(self, position, vertices):
		#base init
		base.__init__(self, position, None, True, True)
		#shape
		self.addPoly(vertices)
		