#!/usr/bin/env python

#python make_egg.py bdist_egg

from setuptools import setup

setup(
    name='derpyDelivery',
    version='0.02.00',
    description='A game based on the MLP:FiM background pony Derpy Hooves.',
    author='Erik Soma',
    author_email='stillusingirc@gmail.com',
    url='http://wiki.secondlife.com/wiki/Eventlet',
    packages=['derpyDelivery'],
	data_files=[
		('img', []),
		('snd', []),
		('font', []),
	],
	classifiers=[
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python",
		"Development Status :: Beta",
		"Topic :: My Little Pony"],
	keywords='derpy hooves pony friendship magic',
	license='GPL',
	install_requires=['pygame', 'pymunk']
	)