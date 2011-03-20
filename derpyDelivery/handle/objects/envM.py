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
from math import copysign, fabs, pi
from derpyDelivery import cfg
import derpyM
import pymunk
from dynamicBlockM import depthBlock
#testing
import pygame.draw
import pygame.rect
import random

#64x64 crate
class crate(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_crate", True, False)
		self.body.mass = 2
		#shape
		self.addRect((0, 0), (64, 64))
		
class rndm(base):
	
	def __init__(self, position, sprite, mass, link = None, linkSprite = None, static = False, finalSprite = None, event = None):
		#base init
		if not static:
			base.__init__(self, position, sprite, True, False)
		else:
			base.__init__(self, position, sprite, False, True)
		self.body.mass = mass
		self.addRect((0, 0), (cfg.imgH.file[sprite][0].get_width(), cfg.imgH.file[sprite][0].get_height()))
		self.defaultSprite = sprite
		self.link = link
		self.linkSprite = linkSprite
		self.timer = 0
		self.finalSprite = finalSprite
		self.event = event
		
	def flip(self):
		pass
		
	def step(self):
		if self.link is not None and self.linkSprite is not None and self.image != self.finalSprite:
			hV = self.link.body.velocity[0]
			if hV < 0:
				hV = -hV
			vV = self.link.body.velocity[1]
			if vV < 0:
				vV = -hV
			combinedVelocity = hV+vV
			if combinedVelocity > 30:
				self.setImage(self.linkSprite)
				self.flip()
				self.timer = 90
				if self.event is not None:
					self.event[0].__dict__[self.event[1]] = True
			else:
				if self.timer <= 0:
					if self.finalSprite is None:
						self.setImage(self.defaultSprite)
					elif self.image == self.linkSprite:
						self.setImage(self.finalSprite)
				else:
					self.timer -= 1

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
		
#mail
class mail(base):
	
	def __init__(self, position):
		#base init
		base.__init__(self, position, "env_mail", True, False)
		self.body.mass = 1
		self.scale = .75
		#shape
		self.shape = self.addRect((0, 0), (29, 21))
		#derpy 
		self.derpyRef = None
		self.arrowIndex = 0
		
	def preStep(self):
		if self.body.velocity[1] > 0:
			self.body.angular_velocity += -copysign(.1, self.body.velocity[0])
		
	def requestPickup(self, other):
		self.derpyRef = other
		
	def draw(self):
		if self.derpyRef is not None:
			if self.derpyRef.canPickUp == self and self.derpyRef.pickedUp is None:
				img = cfg.imgH.file["env_pickuparrow"][self.arrowIndex]
				img.set_alpha(128)
				cfg.window.blit(img, self.body.position-cfg.objH.cam.position-(15, 35))
				self.arrowIndex += 1
				if self.arrowIndex == len(cfg.imgH.file["env_pickuparrow"]):
					self.arrowIndex = 0
					
class muffin(base):
	def __init__(self, position, sprite):
		#base init
		base.__init__(self, position, sprite, True, False)
		self.body.mass = 1
		self.scale = .75
		#shape
		self.shape = self.addRect((0, 0), (cfg.imgH.file[sprite][0].get_width(), cfg.imgH.file[sprite][0].get_height()))
		#derpy 
		self.derpyRef = None
		self.arrowIndex = 0
		
	def preStep(self):
		if self.body.velocity[1] > 0:
			self.body.angular_velocity += -copysign(.1, self.body.velocity[0])
		
	def requestPickup(self, other):
		self.derpyRef = other
		
	def draw(self):
		if self.derpyRef is not None:
			if self.derpyRef.canPickUp == self and self.derpyRef.pickedUp is None:
				img = cfg.imgH.file["env_pickuparrow"][self.arrowIndex]
				img.set_alpha(128)
				cfg.window.blit(img, self.body.position-cfg.objH.cam.position-(15, 35))
				self.arrowIndex += 1
				if self.arrowIndex == len(cfg.imgH.file["env_pickuparrow"]):
					self.arrowIndex = 0
					
					
#bush
class bush(base):

	def __init__(self, position, imgKey):
		#base init
		base.__init__(self, position, imgKey, True, True)
		self.depth = -999
		#shape
		self.shape = self.addRect((0, 30), (124, 74))
		self.imageSpeed = 0
		#derpy collision
		self.collisionEvent(derpyM.derpy, bush.shake)
			
	def shake(self, other, myShapes):
		if self.imageSpeed == 0:
			if (fabs(other.body.velocity[0]) + fabs(other.body.velocity[1])) > 500:
				self.imageSpeed = .25
				self.imageIndex = 1
		
	def step(self):
		if self.imageIndex == 0:
			self.imageSpeed = 0
			
#bird
class birdWithMail(base):

	def __init__(self, position, grabMail):
		base.__init__(self, position, "env_bird_red_r")
		self.shape = self.addRect((10, 5),(32, 24))
		self.imageSpeed = .3
		self.grabMail = grabMail
		if self.grabMail is not None:
			self.grabMail.sensor = True
		self.dir = 1
		self.vdir = 1.0
		self.body.mass = 3
		self.speedMod = 1
		#angle lock
		self.angleLockBody = pymunk.Body(pymunk.inf, pymunk.inf)
		self.angleLock = pymunk.constraint.RotaryLimitJoint(self.body, self.angleLockBody, 0, 0)
		cfg.space.add(self.angleLock)
		
	def step(self):
		#phase counter
		if self.body.position[0] < 2600:
			self.dir = 1
		elif self.body.position[0] > 3400:
			self.dir = -1
		if self.body.position[1] < 200:
			self.vdir = -.2
		elif self.body.position[1] > 600:
			self.vdir = -1
		self.impulse((30*self.dir*self.speedMod, 30*self.vdir))
		if self.dir == 1:
			self.setImage("env_bird_red_r")
		else:
			self.setImage("env_bird_red_l")
		#move mail
		if self.grabMail is not None:
			self.grabMail.set((self.body.position[0]+(30*self.dir), self.body.position[1]))
			if self.grabMail.derpyRef is not None:
				if self.grabMail.derpyRef.pickedUp == self.grabMail:
					self.grabMail = None
					
class bakeryDoor(base):
	def __init__(self, position):
		base.__init__(self, position, "env_stage2_houses_bakery_door", False, True)
		self.depth = 25
		self.imageSpeed = 0
		self.times = 0
		
	def animate(self):
		self.times = 5
		
	def animationEnd(self):
		self.times -= 1
		
	def step(self):
		self.imageSpeed = self.times*.05
		if self.times == 0:
			self.imageIndex = 0
class appleSign(base):
	def __init__(self, position):
		base.__init__(self, position, "env_applestand_sign", False)
		self.addRect((0, 0), (cfg.imgH.file["drwhooves_stand_l"][0].get_width(), cfg.imgH.file["drwhooves_stand_l"][0].get_height()))
		
class appleStand(base):
	def __init__(self, position, sign):
		base.__init__(self, position, "env_applestand")
		self.depth = 20
		self.sign = sign
		self.body.moment = 500
		self.body.mass = 20
		self.addRectImg((-40, 54), (10, 120))
		self.addRectImg((90, 54), (100, 120))
		self.addRectImg((-40, 60), (100, 120))
		con = pymunk.PinJoint(self.body, sign.body, (0, 0), (0, 0))
		cfg.space.add(con)
		self.broken = False
	
	def step(self):
		self.body.moment = 500
		if not self.broken:
			if self.body.angle > 2 or self.body.angle < -2:
				if self.body.velocity[1] < 10 and self.body.velocity[1] > -10:
					self.broken = True
					self.setImage("env_applestand_flipped")
					self.depth = -100
					t = cfg.objH.new(base, (self.body.position[0], self.body.position[1]-20), "env_applestand_top")
					t.addRect((0, 0), (148, 32))
					t.body.angle = self.body.angle
					t.depth = -100
					
class flower(base):
	def __init__(self, position, index):
		base.__init__(self, position, index, False, True)
		self.collisionEvent(derpyM.derpy, flower.crush)
		self.shape = self.addRect((0, 0), (cfg.imgH.file[index][0].get_width(), cfg.imgH.file[index][0].get_height()))
		self.imageSpeed = 0
		
	def crush(self, other, myShapes):
		if other.body.velocity[1] > 150:
			self.imageIndex = 1
			
class scoreKeeperStage2():
	def __init__(self):
		self.flowersCrushed = 0
		self.whoovesHurt = False
		self.mailDelivered = 0
		self.cupcakesEaten = 0
		self.classDisrupted = False
		self.lyraCry = False
		self.bonbonMad = False
		self.appleDestroyed = False
		self.vasesToppled = False
		self.bagTime = 0
		
	def finish(self):
		cfg.rmH.clearRoom()
		l = []
		total = 0
		if self.bagTime > 0:
			l.append(("MAILBAG SAVED", str(int(self.bagTime/30))))
			total += int(self.bagTime/30)
		else:
			l.append(("MAILBAG BURNED", "-15", False))
			total -= 15
		if self.mailDelivered > 0:
			l.append(("MAIL DELIVERED", str(self.mailDelivered*5)))
			total += self.mailDelivered*5
		if self.cupcakesEaten > 0:
			l.append(("MUFFINS EATEN", str(self.cupcakesEaten*2)))
			total += self.cupcakesEaten*2
		if self.flowersCrushed > 0:
			l.append(("FLOWERS CRUSHED", "-"+str(self.flowersCrushed), False))
			total -= self.flowersCrushed
		if self.whoovesHurt:
			l.append(("TRIPPED DR.WHOOVES", "-5", False))
			total -= 5
		if self.classDisrupted:
			l.append(("CLASS DISRUPTED", "-5", False))
			total -= 5
		if self.lyraCry:
			l.append(("MADE LYRA CRY", "-5", False))
			total -= 5
		if self.bonbonMad:
			l.append(("MADE BONBON MAD", "-5", False))
			total -= 5
		if self.appleDestroyed:
			l.append(("APPLE CART DESTROYED", "-5", False))
			total -= 5
		if self.vasesToppled:
			l.append(("FRIGHTENED LILY", "-5", False))
			total -= 5
		l.append(("TOTAL", str(total)))
		cfg.rmH.stageComplete("2", l, cfg.rmH.testRoom)
			
class bagTimer(base):
	def __init__(self, bag, sk):
		base.__init__(self, (0, 0), None, False, True)
		self.bag = bag
		self.sk = sk
		self.textPosition = bag.body.position-cfg.objH.cam.position
		self.scale = 0
		self.depth = -9999
		self.timer = 15*30.0
		self.done = False
		self.helpText = cfg.objH.mediumText.render("The mailbag is on fire! Stomp on it to put it out!", 0, (237, 203, 13), (0, 0, 0))
		self.fade = 0
		self.fadeImage = pygame.surface.Surface((840, 525))
		self.fadeImage.fill((0, 0, 0))
		
	def step(self):
		if not self.done:
			if self.bag.onFire > 0:
				self.timer -= 1
			else:
				self.done = True
				self.sk.bagTime = self.timer
			if self.timer <= 0:
				self.bag.burn()
				self.done = True
		
	def draw(self):
		if self.scale < 1:
			self.scale += .05
		if self.textPosition[0] < 700:
			self.textPosition[0] += 10
		if self.textPosition[1] > 40:
			self.textPosition[1] -= 10
		countdown = None
		if self.done and self.timer <= 0:
			countdown = cfg.objH.largeText.render("0.0", 0, (255, 90, 90), (0, 0, 0))
		else:
			countdown = cfg.objH.largeText.render("%.2f"%(self.timer/30.0), 0, (255, 90, 90), (0, 0, 0))
		countdown = pygame.transform.scale(countdown, (int(countdown.get_width()*self.scale), int(countdown.get_height()*self.scale)))
		cfg.window.blit(countdown, self.textPosition)
		if not self.done:
			cfg.window.blit(self.helpText, (50,500))
		else:
			self.fade += 3
			self.fadeImage.set_alpha(self.fade)
			cfg.window.blit(self.fadeImage, (0, 0))
			if self.fade > 255:
				self.sk.finish()
			
class cookingMailbag(base):
	def __init__(self, position, sk):
		#base init
		base.__init__(self, position, "env_mailbag_cooking", True, False)
		#shape
		self.sk = sk
		self.shape = self.addRect((0, 10), (35, 40))
		#derpy 
		self.derpyRef = None
		self.arrowIndex = 0
		self.swapLayer(2)
		self.depth = 46
		self.body.velocity = (0, 0)
		self.phase = 0
		self.timer = 0
		self.lastdepth = self.depth
		self.onFire = 4
		self.stopCollide = True
		self.colliding = False
		
	def burn(self):
		g = cfg.objH.new(smoke, self.body.position)
		g.depth = self.depth
		g.swapLayer(self.currentLayer)
		g = cfg.objH.new(smoke, self.body.position)
		g.depth = self.depth
		g.swapLayer(self.currentLayer)
		g = cfg.objH.new(smoke, self.body.position)
		g.depth = self.depth
		g.swapLayer(self.currentLayer)
		cfg.sndH.play("effects_highwobble")
		self.destroy()
		if self.derpyRef.pickedUp == self:
			self.derpyRef.pickedUp = None
		if self.derpyRef.canPickUp == self:
			self.derpyRef.canPickUp = None
		
	def preStep(self):
		if self.body.velocity[1] > 0:
			self.body.angular_velocity += -copysign(.1, self.body.velocity[0])
			
	def putOut(self, other, myShapes):
		self.colliding = True
		if self.phase == 1 and self.derpyRef.pickedUp != self and self.stopCollide:
			if self.derpyRef.body.velocity[1] > 250:
				cfg.sndH.play("effects_clonk")
				self.stopCollide = False
				self.onFire -= 1
				if self.onFire <= 0:
					self.setImage("env_mailbag_laying_l")
					self.phase = 2
					cfg.sndH.play("effects_onk")
			
	def step(self):
		if self.phase == 0:
			self.body.velocity = (0, 0)
		elif self.phase == 1:
			if self.timer < 0:
				g = cfg.objH.new(smoke, self.body.position)
				g.depth = self.depth
				g.scale /= 2
				g.swapLayer(self.currentLayer)
				self.timer = 20/self.onFire
			self.timer -= 1
		if self.derpyRef is not None:
			if self.derpyRef.canPickUp == self and self.derpyRef.pickedUp is None:
				self.lastdepth = self.depth
				self.depth = -99
				if self.currentLayer == 2:
					self.alpha = 128
			
		
	def requestPickup(self, other):
		self.derpyRef = other
	
	def draw(self):
		if self.derpyRef is not None:
			if self.derpyRef.canPickUp == self and self.derpyRef.pickedUp is None:
				img = cfg.imgH.file["env_pickuparrow"][self.arrowIndex]
				img.set_alpha(128)
				cfg.window.blit(img, self.body.position-cfg.objH.cam.position-(10, 30))
				self.arrowIndex += 1
				if self.arrowIndex == len(cfg.imgH.file["env_pickuparrow"]):
					self.arrowIndex = 0
			elif self.derpyRef.pickedUp == self and self.phase == 0:
				self.phase = 1
				cfg.objH.new(bagTimer, self, self.sk)
		self.depth = self.lastdepth
		self.alpha = 255
		if not self.colliding:
			self.stopCollide = True
		self.colliding = False
			
class oven(base):
	def __init__(self, position):
		base.__init__(self, position, "env_oven", True, True)
		self.open = False
		self.depth = 45
		self.near = False
		self.arrowIndex = 0
		self.addRect((0, 0), (100, 40))
		self.remRect = self.addRect((50, 40), (70, 260))
		self.swapLayer(2)
		
	def requestOpen(self, other):
		self.near = True
		
	def openUp(self):
		if not self.open:
			self.near = False
			self.open = True
			self.setImage("env_oven_open")
			cfg.space.remove_static(self.remRect)
			cfg.sndH.play("effects_open")
		
	def draw(self):
		if self.near:
			img = cfg.imgH.file["env_pickuparrow"][self.arrowIndex]
			img.set_alpha(128)
			cfg.window.blit(img, self.body.position-cfg.objH.cam.position-(-5, 18))
			self.arrowIndex += 1
			if self.arrowIndex == len(cfg.imgH.file["env_pickuparrow"]):
				self.arrowIndex = 0
		self.near = False
			
class smokeMaker(base):
	def __init__(self, position, bag):
		base.__init__(self, position, None, False, True)
		self.timer = 10
		self.bag = bag
	
	def step(self):
		if self.bag.phase == 1:
			self.destroy()
		self.timer -= 1
		if self.timer <= 0:
			self.timer = 10
			cfg.objH.new(smoke, self.body.position).depth = -100
			
class smoke(base):
	def __init__(self, position):
		base.__init__(self, position, "env_smoke", False, False)
		self.body.angle = random.randrange(0, 22)/7.0
		self.shape = self.addRect((0, 0), (1, 1))
		self.alpha = 128
		self.scale = random.random()+.5
		self.collisionEvent(depthBlock, smoke.destroy)
		
	def step(self):
		self.alpha -= .5
		if self.body.velocity[1] > -10:
			self.force((-random.random()*10, -100*random.random()))
		self.body.angle += .05
		if self.alpha <= 0:
			self.destroy()
#
class mailAlert(base):
	def __init__(self, parent, derpy, offset = (20 , -50)):
		base.__init__(self, (0, 0), "env_mailalert_r", False, False)
		self.imageSpeed = .02
		self.parent = parent
		self.derpy = derpy
		self.offset = offset
		self.shape = self.addRect((0, 0), (cfg.imgH.file["env_mailalert_r"][0].get_width(), cfg.imgH.file["env_mailalert_r"][0].get_height()))
		self.collisionEvent(derpyM.derpy, mailAlert.tellInRange)
		
	def tellInRange(self, other, myShapes):
		other.canDeliver = self
		
	def step(self):
		if self.parent.needMail:
			offset = 0
			if self.parent.dir > 0:
				offset = self.offset[0]
				self.setImage("env_mailalert_r")
			else:
				offset = self.offset[1]
				self.setImage("env_mailalert_l")
			self.body.position = (self.parent.body.position[0]+offset, self.parent.body.position[1]-40)
		else:
			self.destroy()
		
	def animationEnd(self):
		xDis = self.body.position[0]-self.derpy.body.position[0]
		yDis = self.body.position[1]-self.derpy.body.position[1]
		if xDis < 0:
			xDis = -xDis
		if yDis < 0:
			yDis = -yDis
		tDis = xDis+yDis
		if tDis > 900:
			tDis = 900
		vol = (-tDis/900.0)+1
		if vol >= 0.1:
			cfg.sndH.play("effects_sparkle", vol)

class depthPortal(base):
	def __init__(self, position, animator = None):
		base.__init__(self, position, None, False, True)
		self.smallShape = self.addCircle(10)
		self.largeShape = self.addCircle(40)
		self.collisionEvent(derpyM.derpy, depthPortal.detection)
	
		self.leftOuter = True
		self.outerStatus = False
		
		self.animator = animator
		
		self.swapLayer(3)
	
		#testing
		self.position = position
		
	def detection(self, other, myShapes):
		if myShapes[0] == self.smallShape and self.leftOuter:
			if self.animator is not None:
				self.animator.animate()
			self.leftOuter = False
			if other.depth != 50:
				other.depth = 50
				other.swapLayer(2)
				if other.pickedUp is not None:
					other.pickedUp.depth = 50
					other.pickedUp.lastdepth = 50
					other.pickedUp.swapLayer(2)
			else:
				other.depth = -50
				other.swapLayer(1)
				if other.pickedUp is not None:
					other.pickedUp.depth = -50
					other.pickedUp.lastdepth = -50
					other.pickedUp.swapLayer(1)
		else:
			self.outerStatus = True
	
	def step(self):
		if not self.outerStatus:
			self.leftOuter = True
		self.outerStatus = False
		
	def draw(self):
		pass
		"""
		pos = (self.position[0]-cfg.objH.cam.position[0],self.position[1]-cfg.objH.cam.position[1])
		pygame.draw.circle(cfg.window, (0, 255, 0), pos, 40)
		pygame.draw.circle(cfg.window, (0, 255, 255), pos, 10)
		"""
#	
class depthConverter(base):
	def __init__(self, position, height, lToR = False):
		base.__init__(self, position, None, False, True)
		self.lShape = self.addRect((-40, 0), (8, height))
		self.rShape = self.addRect((32, 0), (8, height))
		self.collisionEvent(derpyM.derpy, depthConverter.detection)
		self.collisionEvent(rndm, depthConverter.rndmD)
		self.leftActive = False
		self.rightActive = False
		self.lastLeft = False
		self.lastRight = False
		self.lToR = lToR
		self.derpyObj = None
		self.swapLayer(3)
		
		self.rndms = {}
		
		#testing
		self.depth = -9999
		self.position = position
		self.height = height
					
	def detection(self, other, myShapes):
		self.derpyObj = other
		for shape in myShapes:
			if shape == self.lShape:
				self.leftActive = True
			elif shape == self.rShape:
				self.rightActive = True
				
	def rndmD(self, other, myShapes):
		if not id(other) in self.rndms:
			self.rndms[id(other)] = [False, False, False, False, other]
		for shape in myShapes:
			if shape == self.lShape:
				self.rndms[id(other)][0] = True
			elif shape == self.rShape:
				self.rndms[id(other)][1] = True
				
	def step(self):
		if self.derpyObj is not None:
			if self.rightActive and not self.leftActive and self.lastLeft:
				if self.lToR:
					self.derpyObj.depth = -50
					self.derpyObj.swapLayer(1)
					if self.derpyObj.pickedUp is not None:
						self.derpyObj.pickedUp.depth = -50
						self.derpyObj.pickedUp.swapLayer(1)
				else:
					self.derpyObj.depth = 50
					self.derpyObj.swapLayer(2)
					if self.derpyObj.pickedUp is not None:
						self.derpyObj.pickedUp.depth = 50
						self.derpyObj.pickedUp.swapLayer(2)
			elif self.leftActive and not self.rightActive and self.lastRight:
				if self.lToR:
					self.derpyObj.depth = 50
					self.derpyObj.swapLayer(2)
					if self.derpyObj.pickedUp is not None:
						self.derpyObj.pickedUp.depth = 50
						self.derpyObj.pickedUp.swapLayer(2)
				else:
					self.derpyObj.depth = -50
					self.derpyObj.swapLayer(1)
					if self.derpyObj.pickedUp is not None:
						self.derpyObj.pickedUp.depth = -50
						self.derpyObj.picedkUp.swapLayer(1)
		self.lastLeft = self.leftActive
		self.lastRight = self.rightActive
		self.leftActive = False
		self.rightActive = False
		
		for r in self.rndms:
			s = self.rndms[r]
			leftActive = s[0]
			rightActive = s[1]
			lastLeft = s[2]
			lastRight = s[3]
			if rightActive and not leftActive and lastLeft:
				if self.lToR:
					s[4].depth = -50
					s[4].swapLayer(3)
				else:
					s[4].depth = 50
					s[4].swapLayer(2)
			elif leftActive and not rightActive and lastRight:
				if self.lToR:
					s[4].depth = 50
					s[4].swapLayer(2)
				else:
					s[4].depth = -50
					s[4].swapLayer(3)
			s[2] = s[0]
			s[3] = s[1]
			s[0] = False
			s[1] = False
		
	def draw(self):
		pass
		"""
		pos = (self.position[0]-40-cfg.objH.cam.position[0],self.position[1]-(self.height/2)-cfg.objH.cam.position[1])
		pygame.draw.rect(cfg.window, (0, 0, 255), pygame.rect.Rect(pos, (88, self.height)), 1)
		"""
		