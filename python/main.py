import pygame
from window import Window
from player import player


pygame.init()


window = Window()
player = player.Player()


class Main:
	def __init__(self):
		self.running = True


	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			window.fill()
			pygame.display.flip()


main = Main()


if __name__ == "__main__":
	main.run()
