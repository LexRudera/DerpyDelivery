#!/usr/bin/env python

#python setup.py install

from distutils.core import setup
import os


imgFiles = []
print "Getting img files."
for path, x, files in os.walk('img'):
	for f in files:
		imgFiles.append(os.path.join(path, f))
		
sndFiles = []
print "Getting snd files."
for path, x, files in os.walk('snd'):
	for f in files:
		sndFiles.append(os.path.join(path, f))
		
fntFiles = []
print "Getting fnt files."
for path, x, files in os.walk('font'):
	for f in files:
		fntFiles.append(os.path.join(path, f))

setup(
    name = 'derpyDelivery',
    version = '0.02.00',
    description = 'A game based on the MLP:FiM background pony Derpy Hooves.',
    author = 'Erik Soma',
    author_email = 'stillusingirc@gmail.com',
    url = 'http://www.hamalonesandwich.com/derpydelivery',
    packages = ['derpyDelivery', 'derpyDelivery.handle', 'derpyDelivery.handle.objects'],
	package_data = {'derpyDelivery' : imgFiles + sndFiles + fntFiles},
	classifiers = [
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python",
		"Development Status :: Beta",
		"Topic :: My Little Pony"],
	keywords = 'derpy hooves pony friendship magic',
	license = 'GPL',
	requires = ['pygame', 'pymunk'],
	scripts = ['run_derpy_delivery.py']
	)