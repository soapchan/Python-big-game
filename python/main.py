import pygame
from window import Window
from player import player
from environment import platform


pygame.init()


clock = pygame.time.Clock()
window = Window()
grass = platform.Platform(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Assets\grass.png", 0, 470, 0, True, 40, 40)
player = player.Player(x=50, y=350, xvel=0, yvel=0, width=64, height=64, mode="idle", falling=True, gravity=2)


class Main:
	def __init__(self):
		self.running = True


	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						player.mode = "jump"
						player.jump()

			window.fill()
			player.fall()
			grass.floor_print()
			player.action()
			pygame.display.flip()

			clock.tick(window.tickrate)

main = Main()


if __name__ == "__main__":
	main.run()
