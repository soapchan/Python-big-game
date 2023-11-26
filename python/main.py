import pygame
from window import Window


pygame.init()


window = Window()


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
