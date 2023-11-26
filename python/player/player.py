import pygame


class Player:
	def __init__(self, x, y, vel):
		self.width = 35
		self.height = 48
		self.x = x
		self.y = y
		self.vel = vel


	def Idle(self):
		idle1 = pygame.image.load(r"assets/Character/Idle/Idle-export1.png")
		pygame.time.wait(100)
		idle2 = pygame.image.load(r"assets/Character/Idle/Idle-export2.png")
		pygame.time.wait(100)
		idle3 = pygame.image.load(r"assets/Character/Idle/Idle-export3.png")
		pygame.time.wait(100)
		idle4 = pygame.image.load(r"assets/Character/Idle/Idle-export4.png")
		pygame.time.wait(100)
