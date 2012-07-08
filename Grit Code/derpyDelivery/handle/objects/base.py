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

from math import cos, sin, sqrt, pow, atan2, floor, pi, ceil, fabs, copysign
import inspect
import pygame
import pymunk
from derpyDelivery import cfg

#base class for in game objects
class base():
	
	instances = []
	
	#initializes an object
	#	arguments:
	#		position	- (x, y) tuple defining the position in space for the object
	#		imageKey 	- the key to the image in the Image Handler, see setImage for special details
	#		solid		- whether the object should be calculated for physics collisions
	#		static		- the object does not move, default False
	def __init__(self, position, imageKey = None, solid = True, static = False):
		#create the instances list for this class and its derivatives if it doesn't exist
		#add self to instances list
		if "instances" not in vars(self.__class__):
			self.__class__.instances = []
		self.__class__.instances.append(self)
		#create the
		if self.__class__ != base:
			base.instances.append(self)
		#image
		self.image = None
		self.rect = None
		self.visible = True
		self.depth = 0
		self.alpha = 255
		self.scale = 1
		self.__maxImageIndex = 0
		self.imageIndex = 0
		self.imageSpeed = float(1)
		self.__imageIncrement = float(0)
		self.drawffset = (0, 0)
		self.position = position
		#physics
		self.__static = static
		self.__solid = solid
		self.body = None
		self.shapes = []
		if not self.__static:
			self.body = pymunk.Body(10, 1000)
			cfg.space.add(self.body)
		else:
			self.body = pymunk.Body(pymunk.inf, pymunk.inf)
		self.body.parentObject = self
		#set
		self.set(position)
		self.setImage(imageKey)
		#collisions
		self.solid = False
		self.currentLayer = 1
	
	#flags the object for destruction in the next step
	def postDestroy(self):
		cfg.space.add_post_step_callback(self.destroy, None, None, None)
		
	#destroys the object's physics existence
	def destroy(self, obj = None, *args, **kwargs):
		if self in self.__class__.instances and self in base.instances:
			if cfg.objH.cam.tracker == self:
				cfg.objH.cam.tracker = None
			if self.__class__ != base:
				self.__class__.instances.remove(self)
			base.instances.remove(self)
			if self.__static:
				for shape in self.shapes:
					try:
						cfg.space.remove_static(shape)
					except:
						pass
			else:
				for shape in self.shapes:
					try:
						cfg.space.remove(shape)
					except:
						pass
				cfg.space.remove(self.body)
			self.body.parentObject = None
		
	def getDrawPos(self):
		if self.__static:
			return self.position
		else:
			return self.body.position
		
	#moves an object in space
	#	arguments:
	#		h - how much to move on the x plane
	#		v - how much to move on the y plane
	def move(self, h, v):
		self.body.position = (self.body.position[0] + h, self.body.position[1] + v)
	
	#set the position of the object in space
	#	arguments:
	#		position	- (x, y) tuple defining the position in space for the object
	def set(self, position):
		self.position = position
		self.body.position = (position[0], position[1])
		
	#applies an impulse to the object's body
	#	arguments:
	#		force - the force to apply
	def impulse(self, force):
		if cfg.objH.frameSpeed == 1:
			self.body.apply_impulse((force[0]*2, force[1]*2))
		else:
			self.body.apply_impulse(force)
		
	#applies a force to the object's body
	#	arguments:
	#		force - the force to apply
	def force(self, force):
		if cfg.objH.frameSpeed == 1:
			self.body.apply_force((force[0]*2, force[1]*2))
		else:
			self.body.apply_force(force)
		
	#set collision event
	#	arguments:
	#		objClass 	- the class of the object to check collision against
	#		event		- a function to run when a collision occurs, None to remove collision processing for this class
	#						function must be defined as: def foo(self, other)
	#						where other is the colliding instance
	def collisionEvent(self, objClass, event = None):
		if event != None:
			cfg.space.add_collision_handler(id(self.__class__), id(objClass), None, self.__collisionEventWrapper, None, None, event)
		else:
			cfg.space.remove_collision_handler(id(self.__class__), id(objClass))
	
	#collision event wrapper
	#	arguments:
	#		*args[0] - the event function for the collision
	#	returns:
	#		true if both objects are solid, false otherwise
	def __collisionEventWrapper(declarer, space, arbiter, *args, **kwargs):
		self = None
		event = args[0]
		other = None
		myShapes = []
		for shape in arbiter.shapes:
			if shape is None:
				return False
			if shape.body.parentObject.__class__ == declarer.__class__:
				self = shape.body.parentObject
				myShapes.append(shape)
			else:
				other = shape.body.parentObject
		event(self, other, myShapes)
		if other.__solid and self.__solid:
			return True
		else:
			return False
	
	#animation step processed every loop
	def animateStep(self):
		iSpeed = self.imageSpeed
		if cfg.objH.frameSpeed == 1:
			iSpeed *= 2
		#animate
		if self.__maxImageIndex > 0:												#if has animation
			if self.imageSpeed > 0:													#	if animating
				self.__imageIncrement += iSpeed										#		increment frame counter
				if self.__imageIncrement >= 1:										#		if frame threshold exceeded
					
					self.imageIndex += int(floor(self.__imageIncrement))			#			increases frame index
					self.__imageIncrement -= floor(self.__imageIncrement)			#			reduce frame counter
					if self.imageIndex > self.__maxImageIndex:						#			if frame index exceeds max frame index
						self.animationEnd()
						self.imageIndex = 0											#				frame is back to 0
						
	def animationEnd(self):
		pass
	
	#pre step event processed every loop
	def preStep(self):
		pass
	
	#step event processed every loop
	def step(self):
		pass
	
	#end step event processed every loop
	def endStep(self):
		pass
		
	#draw
	def draw(self):
		pass
	
	#find the x center
	def xCenter(self):
		return float(self.rect.x+(self.rect.width/2))
		
	#find the y center
	def yCenter(self):
		return float(self.rect.y+(self.rect.height/2))
	
	#sets the image of the object
	#	arguments:
	#		imageKey - the key to the image in the Image Handler
	#			when None: image is removed
	#			when DNE: nothing changes
	#	if the Mask hasn't been set yet a mask will be generated from the first frame of the image
	def setImage(self, imageKey):
		if imageKey is not None:
			if imageKey in cfg.imgH.file:
				if self.image != cfg.imgH.file[imageKey]:
					self.image = cfg.imgH.file[imageKey]
					self.__maxImageIndex = len(self.image)-1
					self.imageIndex = 0
		else:
			self.image = None
			self.__maxImageIndex = 0
		
	#add a circle shape to the object body
	#	arguments:
	#		radius - the radius of the circle
	def addCircle(self, radius):
		shape = pymunk.Circle(self.body, radius)
		shape.collision_type = id(self.__class__)
		shape.layers = 1
		if not self.__solid:
			shape.sensor = True
		if not self.__static:
			cfg.space.add(shape)
		else:
			cfg.space.add_static(shape)
		self.shapes.append(shape)
		return shape
			
	#add a line shape to the object body
	#	arguments:
	#		startPoint 	- (x, y) tuple for the start of the line
	#		endPoint	- (x, y) tuple for the end of the line
	#		thickness	- thickness of the line
	def addLine(self, startPoint, endPoint, thickness):
		shape = pymunk.Segment(self.body, startPoint, endPoint, thickness)
		shape.collision_type = id(self.__class__)
		shape.layers = 1
		if not self.__solid:
			shape.sensor = True
		if not self.__static:
			cfg.space.add(shape)
		else:
			cfg.space.add_static(shape)
		self.shapes.append(shape)
		return shape
	
	#add a rectanlge shape to the object body
	#	arguments:
	#	topLeft		- (x, y) tuple for the top left of the rectangle
	#	bottomRight	- (x, y) tuple for the bottom right of the rectangle
	def addRect(self, topLeft, bottomRight):
		width = topLeft[0] - bottomRight[0]
		height = topLeft[1] - bottomRight[1]
		topLeft = (topLeft[0] + width/2, topLeft[1] + height/2)
		bottomRight = (bottomRight[0] + width/2, bottomRight[1] + height/2)
		topRight = (bottomRight[0], topLeft[1])
		bottomLeft = (topLeft[0], bottomRight[1])
		shape = pymunk.Poly(self.body, [topLeft, topRight, bottomRight, bottomLeft], (0, 0))
		shape.collision_type = id(self.__class__)
		shape.layers = 1
		if not self.__solid:
			shape.sensor = True
		if not self.__static:
			cfg.space.add(shape)
		else:
			cfg.space.add_static(shape)
		self.shapes.append(shape)
		return shape
		
	def addRectImg(self, topLeft, bottomRight):
		width = self.image[0].get_width()/2
		height = self.image[0].get_height()/2
		topLeft = (topLeft[0] - width/2, topLeft[1] - height/2)
		bottomRight = (bottomRight[0] - width/2, bottomRight[1] - height/2)
		topRight = (bottomRight[0], topLeft[1])
		bottomLeft = (topLeft[0], bottomRight[1])
		shape = pymunk.Poly(self.body, [topLeft, topRight, bottomRight, bottomLeft], (0, 0))
		shape.collision_type = id(self.__class__)
		shape.layers = 1
		if not self.__solid:
			shape.sensor = True
		if not self.__static:
			cfg.space.add(shape)
		else:
			cfg.space.add_static(shape)
		self.shapes.append(shape)
		return shape
		
	def addPoly(self, vertices):
		shape = pymunk.Poly(self.body, vertices, (0, 0))
		shape.collision_type = id(self.__class__)
		shape.layers = 1
		if not self.__solid:
			shape.sensor = True
		if not self.__static:
			cfg.space.add(shape)
		else:
			cfg.space.add_static(shape)
		self.shapes.append(shape)
		return shape
		
	def swapLayer(self, layerPlane):
		self.currentLayer = layerPlane
		for shape in self.shapes:
			shape.layers = layerPlane