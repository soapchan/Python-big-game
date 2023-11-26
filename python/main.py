import pygame
from window import Window
from player import player
from environment import platform


pygame.init()


window = Window()
platform = platform.Platform(r"assets/Assets/grass.png", 0, 450, 0, True, 500, 50)
player = player.Player(50, 100, 0, 35, 48, "idle")


class Main:
	def __init__(self):
		self.running = True


	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			window.fill()
			player.action()
			pygame.display.flip()


main = Main()


if __name__ == "__main__":
	main.run()
