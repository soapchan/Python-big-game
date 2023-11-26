import pygame
from python.window import Window


window = Window()


class Player:
	def __init__(self, x, y, vel, width, height, mode):
		self.width = 35
		self.height = 48
		self.x = x
		self.y = y
		self.vel = vel
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)
		self.mode = mode
		self.clock = pygame.time.Clock


	def idle(self):
		idle1 = pygame.image.load(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Character\Idle\Idle-export1.png")
		window.display.blit(idle1, (self.x, self.y))
		pygame.time.wait(100)
		pygame.display.flip()
		idle2 = pygame.image.load(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Character\Idle\Idle-export2.png")
		window.display.blit(idle2, (self.x, self.y))
		pygame.time.wait(100)
		pygame.display.flip()
		idle3 = pygame.image.load(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Character\Idle\Idle-export3.png")
		window.display.blit(idle3, (self.x, self.y))
		pygame.time.wait(100)
		pygame.display.flip()
		idle4 = pygame.image.load(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Character\Idle\Idle-export4.png")
		window.display.blit(idle4, (self.x, self.y))
		pygame.time.wait(100)
		pygame.display.flip()


	def action(self):
		if self.mode == "idle":
			self.idle()
