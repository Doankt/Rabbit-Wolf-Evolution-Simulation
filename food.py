import pygame

class Food():
	def __init__(self, world, pos: (int, int)):
		self.world = world
		self.pos = pos

	def draw(self, screen) -> None:
		pygame.draw.circle(screen, (200, 200, 60), self.pos, 5)