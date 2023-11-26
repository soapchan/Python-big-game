import pygame


class Window:
	def __init__(self):
		self.width = 500
		self.height = 500
		self.colour = 255, 255, 255
		self.display = pygame.display.set_mode((self.width, self.height))
		self.tickrate = 60


	def fill(self):
		self.display.fill(self.colour)
