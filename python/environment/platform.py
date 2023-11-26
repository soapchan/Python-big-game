import pygame


class Platform:
	def __init__(self, directory, x, y, vel, collide, width, height):
		self.directory = directory
		self.x = x
		self.y = y
		self.vel = vel
		self. collide = collide
		self.width = width
		self.height = height


	def create(self):
		pass
