import pygame

class Food():
	"""Class representing Food in the world"""

	def __init__(self, world, pos: (float, float)):
		self.world = world
		self.pos = pos

	def draw(self, screen: pygame.Surface) -> None:
		"""
		Draws Rabbit to the screen

		Args:
			screen (pygame.Surface): The pygame surface
		"""

		pygame.draw.circle(screen, (200, 200, 60), self.pos, 5)