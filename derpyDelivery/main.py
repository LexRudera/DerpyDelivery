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

import sys
import pygame
import pymunk
import os
import json
import time
import handle.img
import handle.obj
import handle.key
import handle.room
import handle.snd
import cfg
from math import pi
import traceback
	
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
	cfg.space.gravity = (0, 300)							#default gravity
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
	#load defaults
	cfg.leftButton = str(pygame.K_LEFT)
	cfg.rightButton = str(pygame.K_RIGHT)
	cfg.upButton = str(pygame.K_UP)
	cfg.downButton = str(pygame.K_DOWN)
	cfg.menuButton = str(pygame.K_ESCAPE)
	cfg.startButton = str(pygame.K_SPACE)
	cfg.oneButton = str(pygame.K_z)
	cfg.twoButton = str(pygame.K_x)
	#try to load external settings
	cfgFile = os.path.abspath("config")
	if os.path.isfile(cfgFile):
		f = open(cfgFile, 'r')
		try:
			settings = json.load(f)
			cfg.rightButton = settings["controls"]["right"]
			cfg.upButton = settings["controls"]["up"]
			cfg.leftButton = settings["controls"]["left"]
			cfg.downButton = settings["controls"]["down"]
			cfg.oneButton = settings["controls"]["one"]
			cfg.twoButton = settings["controls"]["two"]
			cfg.startButton = settings["controls"]["start"]
			cfg.menuButton = settings["controls"]["menu"]
			cfg.sndH.musicVolume = float(settings["sound"]["music"])
			cfg.sndH.effectVolume = float(settings["sound"]["effects"])
		except (ValueError, KeyError):
			pass
		f.close()
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
	#set the options menu key
	cfg.keyH.assignKeyPress(cfg.menuButton, cfg.rmH.pause)
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
	print traceback.format_exc()
	__exit()

#loop
#	main game loop
###########################
def __loop():
	
	now = time.clock()		#used to measure FPS
	frame = 0				#counts the frames
	fs = 1.0/(cfg.objH.defFS*cfg.objH.frameSpeed)
	#the main loop
	while True:
		#limits the loop speed
		cfg.clock.tick(cfg.objH.defFS*cfg.objH.frameSpeed)
		
		#FPS counter for testing
		#not 100% accurate
		frame += 1
		if time.clock() - now >= 1:
			now = time.clock()
			pygame.display.set_caption("Derpy Delivery - 0.02.00 FPS: " + str(frame) + "ish")
			frame = 0
			
		#prestep and physics
		if not cfg.objH.paused:
			cfg.objH.preStep()
			cfg.space.step(fs)
			
		#process messages
		__procMsg()
		
		#key process down
		cfg.keyH.process()
		
		#stepping
		if not cfg.objH.paused:
			cfg.objH.step()
			cfg.objH.endStep()
			
		#drawing
		cfg.objH.draw()
		
		#flip display
		pygame.display.update(cfg.objH.cam.getRect())
		
#procMsg
#	processes message
def __procMsg():
	#pygame message
	for event in pygame.event.get():
		if event.type == pygame.QUIT:												#quit
			__exit()
		elif event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:		#keyboard/joystick press
			cfg.keyH.processPress(event)
		elif event.type == pygame.KEYUP or event.type == pygame.JOYBUTTONUP:		#keyboard/joystick release
			cfg.keyH.processRelease(event)
		elif event.type == pygame.JOYAXISMOTION:									#joystick analog axis
			cfg.keyH.processAnalog(event)
		else:																		#other
			pass
			