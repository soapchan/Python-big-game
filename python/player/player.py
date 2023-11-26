import pygame
from .. import window


window = window.Window()


class Player:
	def __init__(self, x, y, vel, width, height):
		self.width = 35
		self.height = 48
		self.x = x
		self.y = y
		self.vel = vel
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)


	def Idle(self):
		idle1 = pygame.image.load(r"assets/Character/Idle/Idle-export1.png")
		window.display.blit(idle1, self.x, self.y)
		pygame.time.wait(100)
		idle2 = pygame.image.load(r"assets/Character/Idle/Idle-export2.png")
		window.display.blit(idle2, self.x, self.y)
		pygame.time.wait(100)
		idle3 = pygame.image.load(r"assets/Character/Idle/Idle-export3.png")
		window.display.blit(idle3, self.x, self.y)
		pygame.time.wait(100)
		idle4 = pygame.image.load(r"assets/Character/Idle/Idle-export4.png")
		window.display.blit(idle4, self.x, self.y)
		pygame.time.wait(100)
