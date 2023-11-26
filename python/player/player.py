import pygame


class Player:
	def __init__(self, x, y, vel):
		self.width = 35
		self.height = 48
		self.x = x
		self.y = y
		self.vel = vel
