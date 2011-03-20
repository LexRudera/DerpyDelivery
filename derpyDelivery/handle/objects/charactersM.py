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
from envM import mail, rndm
from math import ceil
import derpyM

#horte
class horte(base):
	def __init__(self, position):
		base.__init__(self, position, "horte_r", False, True)
		self.timer = 30*7
		self.dir = 1
		
	def step(self):
		self.timer -= 1
		if self.timer < 0:
			if self.dir == 1:
				self.setImage("horte_l")
			else:
				self.setImage("horte_r")
			self.dir = -self.dir
			self.timer = 30*8
			
#mscake
class mscake(base):
	def __init__(self, position):
		base.__init__(self, position, "mscake_stand_r", False, True)
		self.timer = 30*3
		self.dir = 1
		
	def step(self):
		self.timer -= 1
		if self.timer < 0:
			if self.dir == 1:
				self.setImage("mscake_stand_l")
			else:
				self.setImage("mscake_stand_r")
			self.dir = -self.dir
			self.timer = 30*3

#daisy
class daisy(base):
	def __init__(self, position, flowers, sk):
		base.__init__(self, position, "daisy_stand_r", False, True)
		self.sk = sk
		self.flowers = flowers
		self.crushed = []
		self.depth = 30
		self.timer = 30*4
		self.timer2 = 30*8
		self.timer3 = 0
		self.walking = False
		self.sniffing = False
		self.sniff = 0
		self.dir = 1
		self.sad = False
		dP = (cfg.imgH.file["daisy_stand_r"][0].get_height()/2)+self.position[1]
		for f in flowers:
			f.depth = self.depth+(dP-(f.body.position[1]+cfg.imgH.file["flower_white"][0].get_height()/2))
		
	def startSniff(self):
		self.timer3 = 30*3
		self.sniff = 1
		self.imageSpeed = .05
		if self.dir > 0:
			self.setImage("daisy_sniff_r")
		else:
			self.setImage("daisy_sniff_l")
		self.animationEnd = self.passOverride
		
	def endSniff(self):
		self.animationEnd = self.passOverride
		self.sniff = 0
		self.sniffing = False
		self.timer2 = 30*12
		
	def passOverride(self):
		pass
		
	def step(self):
		for flower in self.flowers:
			if flower.imageIndex == 1:
				if not flower in self.crushed:
					self.crushed.append(flower)
					if len(self.crushed) > 4:
						self.sad = True
		self.sk.flowersCrushed = len(self.crushed)
		if not self.sad:
			self.timer -= 1
			self.timer2 -= 1
			self.timer3 -= 1
			if self.timer <= 0:
				if not self.walking:
					self.walking = True
					self.timer = 30*18
				else:
					self.walking = False
					self.timer = 30*6
		
			if self.timer2 <= 0 and not self.sniffing:
				self.sniffing = True
			if self.sniffing:
				self.drawffset = (0, 0)
				if self.sniff == 0:
					self.animationEnd = self.startSniff
					self.imageSpeed = .15
					if self.dir > 0:
						self.setImage("daisy_sniff_start_r")
					else:
						self.setImage("daisy_sniff_start_l")
				elif self.sniff == 1:
					if self.timer3 < 0:
						self.sniff = 2
						self.animationEnd = self.endSniff
				elif self.sniff == 2:
					self.imageSpeed = .15
					if self.dir > 0:
						self.setImage("daisy_sniff_end_r")
					else:
						self.setImage("daisy_sniff_end_l")
			elif self.walking:
				self.imageSpeed = .2
				if self.dir > 0:
					self.drawffset = (-13, 0)
					self.setImage("daisy_walk_r")
					self.body.position[0] += 1.2
					if self.body.position[0] > 700:
						self.dir = -1
				else:
					self.drawffset = (13, 0)
					self.setImage("daisy_walk_l")
					self.body.position[0] -= 1.2
					if self.body.position[0] < 200:
						self.dir = 1
			else:
				self.drawffset = (0, 0)
				if self.dir > 0:
					self.setImage("daisy_stand_r")
				else:
					self.setImage("daisy_stand_l")
		else:
			self.drawffset = (0, 0)
			if self.dir > 0:
				self.setImage("daisy_sad_r")
			else:
				self.setImage("daisy_sad_l")
#lily
class lily(base):
	def __init__(self, position, vases, sk):
		base.__init__(self, position, "lily_stand", False, True)
		self.vases = vases
		self.depth = 50
		self.freak = False
		self.sk = sk
		
	def step(self):
		if not self.freak:
			for vase in self.vases:
				if vase.body.velocity[1] > 50:
					self.sk.vasesToppled = True
					self.freak = True
					self.setImage("lily_gasp")
		else:
			if self.body.angle > -1.5:
				self.body.angle -= 0.075
				self.body.position[1] += 0.75
				self.body.position[0] += 0.75
			else:
				if self.body.position[1] < 1875:
					self.body.angle -= 0.02
					self.body.position[1] += 1

#applebloom
class applebloom(base):
	def __init__(self, position, derpy, applestand, sk):
		base.__init__(self, position, "applebloom_stand_l", False, True)
		self.derpy = derpy
		self.applestand = applestand
		self.imageSpeed = .1
		self.sk = sk
		
	def step(self):
		if self.derpy.body.position[0] < self.body.position[0]:
			if self.applestand.broken:
				self.sk.appleDestroyed = True
				self.setImage("applebloom_stomp_l")
			else:
				self.setImage("applebloom_stand_l")
		else:
			if self.applestand.broken:
				self.sk.appleDestroyed = True
				self.setImage("applebloom_stomp_r")
			else:
				self.setImage("applebloom_stand_r")
#dr whooves
class drhooves(base):

	def __init__(self, position, sk):
		base.__init__(self, position, "drwhooves_stand_l", False, False)
		self.imageSpeed = .2
		self.addRect((0, 0), (cfg.imgH.file["drwhooves_stand_l"][0].get_width(), cfg.imgH.file["drwhooves_stand_l"][0].get_height()))
		self.phase = 0
		self.origin = position
		self.depth = 10
		self.collisionEvent(derpyM.derpy, drhooves.push)
		self.dir = -1
		self.needMail = True
		self.sk = sk
		
	def getMail(self):
		self.needMail = False
		self.setImage("drwhooves_hasmail")
		self.sk.mailDelivered += 1
		
	def push(self, other, myShapes):
		if self.phase == 0:
			self.sk.whoovesHurt = True
			xV = other.body.velocity[0]
			if xV < 0:
				xV = -xV
			yV = other.body.velocity[1]
			if yV < 0:
				yV = -yV
			t = xV+yV
			if t > 500:
				if not self.needMail:
					cfg.objH.new(mail, self.body.position)
				else:
					self.needMail = False
				self.phase = 1
				self.setImage("drwhooves_fall")
				self.body.angular_velocity = 15
				cfg.sndH.play("effects_beooo")
				
		
	def step(self):
		if self.phase == 0:
			self.set(self.origin)
		elif self.phase == 1:
			self.force((0, 40))
			if self.body.position[1] >= 1900:
				self.phase = 2
				self.origin = (self.body.position[0], self.body.position[1])
				self.set(self.origin)
				self.body.angle = 0
				self.setImage("drwhooves_hurt")
				self.body.velocity = (0, 0)
				cfg.sndH.play("effects_clonk")
		elif self.phase == 2:
			self.set(self.origin)
#mayor
class mayor(base):

	def __init__(self, position, sk):
		#base init
		base.__init__(self, position, "mayor_walk_l", False, False)
		self.imageSpeed = .175
		self.sk = sk
		self.addRect((0, 0), (cfg.imgH.file["mayor_walk_l"][0].get_width(), cfg.imgH.file["mayor_walk_l"][0].get_height()))
		self.dir = -1
		self.yOrigin = position[1]
		self.depth = -20
		self.needMail = True
		
	def getMail(self):
		self.needMail = False
		if self.dir == 1:
			self.setImage("mayor_stand_hasmail_r")
		else:
			self.setImage("mayor_stand_hasmail_l")
		self.body.velocity = (0, 0)
		self.sk.mailDelivered += 1
		
	def step(self):
		if self.needMail:
			if self.position[0] < 1000:
				self.dir = 1
				self.setImage("mayor_walk_r")
			elif self.position[0] > 6000:
				self.dir = -1
				self.setImage("mayor_walk_l")
			self.set((self.position[0]+(.85*self.dir), self.yOrigin))
		else:
			self.body.velocity = (0, 0)
			
class cheerilee(rndm):
	def __init__(self, position, tt, sk):
		rndm.__init__(self, position, "cheerilee_stand_r", 3, tt, "cheerilee_gasp_r", True)
		self.needMail = True
		self.dir = 1
		self.sk = sk
		self.addRect((0, 0), (cfg.imgH.file["cheerilee_stand_r"][0].get_width(), cfg.imgH.file["cheerilee_stand_r"][0].get_height()))
		
	def flip(self):
		self.sk.classDisrupted = True
		
	def getMail(self):
		self.needMail = False
		self.sk.mailDelivered += 1
		self.setImage("cheerilee_stand_hasmail")
		self.linkSprite = "cheerilee_stand_hasmail"
		self.defaultSprite = "cheerilee_stand_hasmail"
		
		

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
		self.mailCount = 0
		self.timer = 60*60
		
	def collectMail(self, other, myShapes):
		if self.derpyRef.pickedUp != other:
			other.postDestroy()
			cfg.sndH.play("effects_sparkle")
			self.mailCount += 1
		
	def step(self):
		if self.mailCount == 3:
			t = int(ceil(self.timer/60.0))
			if t < 0:
				t = 0
			cfg.rmH.clearRoom()
			cfg.rmH.stageComplete("1", [("TIME", str(t)), ("TOTAL", str(t))], cfg.rmH.stageTwoCutscene)
		if cfg.objH.frameSpeed == 1:
			self.timer -= 2
		else:
			self.timer -= 1
		self.set(self.slewPos)
		if self.derpyRef.body.position[0] < self.body.position[0]:
			self.setImage("boxhorse_fly_wait_l")
		elif self.derpyRef.body.position[0] > self.body.position[0]:
			self.setImage("boxhorse_fly_wait_r")