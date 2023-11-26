import pygame
from window import Window
from player import player
from environment import platform


pygame.init()


window = Window()
grass = platform.Platform(r"C:\Users\noahf\Desktop\python-all\Python-big-game\assets\Assets\grass.png", 0, 470, 0, True, 40, 40)
player = player.Player(50, 390, 0, 0, 64, 64, "idle")


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
			grass.floor_print()
			player.action()
			pygame.display.flip()


main = Main()


if __name__ == "__main__":
	main.run()
