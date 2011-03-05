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
import pymunk
from derpyDelivery import cfg
from env import mail

#box brown
class boxBrown(base):
	
	def __init__(self, position, derpyRef):
		#base init
		base.__init__(self, position, "boxhorse_fly_wait_l")
		self.body.mass = 20
		self.imageSpeed = .2
		#shape
		self.addRect((0, 0), (124, 132))
		#movepos
		self.slewPos = position
		self.derpyRef = derpyRef
		#angle lock
		self.angleLockBody = pymunk.Body(pymunk.inf, pymunk.inf)
		self.angleLock = pymunk.constraint.RotaryLimitJoint(self.body, self.angleLockBody, 0, 0)
		cfg.space.add(self.angleLock)
		#mail collision
		self.collisionEvent(mail, boxBrown.collectMail)
		
	def collectMail(self, other):
		if self.derpyRef.pickedUp != other:
			other.postDestroy()
			cfg.sndH.play("effects_sparkle")
		
	def step(self):
		self.set(self.slewPos)
		if self.derpyRef.body.position[0] < self.body.position[0]:
			self.setImage("boxhorse_fly_wait_l")
		elif self.derpyRef.body.position[0] > self.body.position[0]:
			self.setImage("boxhorse_fly_wait_r")