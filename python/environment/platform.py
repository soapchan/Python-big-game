import pygame
from python.window import Window


window = Window()


class Platform:
	def __init__(self, directory, x, y, vel, collide, width, height):
		self.directory = directory
		self.x = x
		self.y = y
		self.vel = vel
		self.collide = collide
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)


	def create(self):
		image = pygame.image.load(self.directory)
		window.display.blit(image, (self.x, self.y))


	def floor_print(self):
		count = window.width // self.width
		print(count)
		image = pygame.image.load(self.directory)
		for i in range(count):
			x = i * self.width
			window.display.blit(image, (x, self.y))
			self.x += self.x
