import pygame
from python.window import Window
from python.environment import platform


grass = platform.Platform(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Assets\grass.png", 0, 450, 0, True, 40, 40)
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
		count = 1
		for i in range(4):
			idle1 = pygame.image.load(fr"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Character\Idle\Idle{count}.png")
			window.display.blit(idle1, (self.x, self.y))
			pygame.time.wait(100)
			count += 1


	def action(self):
		if self.mode == "idle":
			self.idle()
		if self.mode == "jump":
			self.jump()


	def jump(self):
		count = 15
		for i in range(count):
			i += 1
			jump1 = pygame.image.load(rf"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Character\Jumlp-All\Jump-All{i}.png")
			window.fill()
			grass.floor_print()
			window.display.blit(jump1, (self.x, self.y))
			pygame.display.flip()
			pygame.time.wait(100)
			i += 1
		self.mode = "idle"
