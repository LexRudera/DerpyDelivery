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

try:
	import sys
	import pygame
	import pymunk
	import os
	import time
	import handle.img
	import handle.obj
	import handle.key
	import handle.room
	import handle.snd
	import cfg
	from math import pi
	import traceback
	
	
except ImportError, err:
	print "Failed to load Module. %s" % (err)
	sys.exit(2)
	
#go
#	run game
###########################
def go():
	try:
		__init()
		__load()
		__loop()
		__exit()
	except Exception, ex:
		__exception(ex)
	
#initalization
#	init system
###########################
def __init():
	
	#PYGAME INIT
	pygame.init()
	pygame.font.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'					#Center Window
	
	#PYMUNK INIT
	pymunk.init_pymunk()
	cfg.space = pymunk.Space()
	cfg.space.gravity = (0, 300)						#default gravity
	cfg.space.damping = .2
	
	#WINDOW
	cfg.window = pygame.display.set_mode((840, 525))		#Window Size
	cfg.window.fill((0,0,0))
	pygame.display.set_caption("Derpy Delivery!")			#Window Caption
	pygame.mouse.set_visible(0)								#Mouse Off
	
	#CLOCK
	cfg.clock = pygame.time.Clock()
	
	#IMAGE HANDLER
	cfg.imgH = handle.img.handler()
	
	#SOUND HANDLER
	cfg.sndH = handle.snd.handler()
	
	#KEYBOARD HANDLER
	cfg.keyH = handle.key.handler()
	
	#OBJECT HANDLER
	cfg.objH = handle.obj.handler()
	
	#ROOM HANDLER
	cfg.rmH = handle.room.handler()
	
#load
#	import external resources
###########################
def __load():
	loadingImages = True
	loadingSounds = True
	#load images
	while loadingImages:
		__procMsg()	#process messages
		cfg.window.fill((0,0,0))	#fill window
		loadedImage = cfg.imgH.load()
		if loadedImage is not None:
			cfg.window.blit(cfg.objH.mediumText.render("Loading Images...", 0, (237, 203, 13)), (150,250))
			cfg.window.blit(cfg.objH.smallText.render(loadedImage, 0, (237, 203, 13)), (450,255))
			pygame.display.flip()
		else:
			loadingImages = False
	#load sounds
	while loadingSounds:
		__procMsg() #process messages
		cfg.window.fill((0,0,0))	#fill window
		loadedSound = cfg.sndH.load()
		if loadedSound is not None:
			cfg.window.blit(cfg.objH.mediumText.render("Loading Sounds...", 0, (237, 203, 13)), (150,250))
			cfg.window.blit(cfg.objH.smallText.render(loadedSound, 0, (237, 203, 13)), (450,255))
			pygame.display.flip()
		else:
			loadingSounds = False
	#set default room
	cfg.rmH.mainMenu()
#exit
#	graceful exit
###########################
def __exit():
	pygame.quit()
	sys.exit(2)
	
#exception
#	handle exceptions
###########################
def __exception(ex):
	f = open('exceptions.txt', 'a')
	f.write("Error Report:\n")
	f.write("TIME: " + str(time.localtime().tm_year) + "-" + str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_mday) + "  " + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec) + "\n")
	f.write("TYPE: " + str(sys.exc_info()[0])+"\n")
	f.write("MSG: " + str(sys.exc_info()[1])+"\n")
	f.write("TRACE: " + traceback.format_exc()+"\n")
	f.write("\n")
	f.closed
	__exit()

#loop
#	main game loop
###########################
def __loop():
	
	now = time.clock()		#used to measure FPS
	frame = 0				#counts the frames
	spaceStepSize = 1/60.0
	
	#the main loop
	while True:
		#limits the loop speed
		cfg.clock.tick(60)
		
		#FPS counter for testing
		#not 100% accurate
		frame += 1
		if time.clock() - now >= 1:
			now = time.clock()
			pygame.display.set_caption("Derpy Delivery Alpha 0.0! FPS: " + str(frame))
			frame = 0 
		
		#process messages
		__procMsg()
		
		#key process down
		cfg.keyH.process()
		#stepping
		cfg.space.step(spaceStepSize)
		cfg.objH.step()
		#drawing
		cfg.objH.draw()
		
		#flip display
		pygame.display.flip()
		
#procMsg
#	processes message
def __procMsg():
	#pygame message
	for event in pygame.event.get():
		if event.type == pygame.QUIT:			#quit
			__exit()
		elif event.type == pygame.KEYDOWN:		#keyboard press
			cfg.keyH.processPress(event)
		elif event.type == pygame.KEYUP:		#keyboard release
			cfg.keyH.processRelease(event)
		else:									#other
			pass
			