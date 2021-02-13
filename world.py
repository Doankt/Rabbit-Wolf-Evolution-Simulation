import random
import pygame
from rabbit import Rabbit
from wolf import Wolf
from food import Food

class World():
	"""Class representing an environment"""

	def __init__(self, srn_sz: (float, float), clock: pygame.time.Clock, screen: pygame.Surface):
		"""
		Initializes the World

		Args:
			srn_sz ( (float, float) ): Screen size
			clock (pygame.time.Clock): pygame Clock
			screen (pygame.Surface): pygame Screen
		"""

		self.running = True

		self._clock = clock
		self.screen = screen
		
		self.runtime = 0
		self.runtime_checkpoint = 0

		self.size = srn_sz
		self.rabbits = []
		self.wolves = []
		self.food = []

		for _ in range(20):
			self.rabbits.append(Rabbit(self, self._random_pos(), 2.5))

		for _ in range(6):
			self.wolves.append(Wolf(self, self._random_pos(), 3.0))

		for _ in range(80):
			self.food.append(Food(self, self._random_pos()))

		self._update_screen()

	
	def step(self) -> None:
		"""
		Advances the world by one frame
		"""

		# Add food every time frame
		self.runtime += self._clock.get_time()
		if (self.runtime - self.runtime_checkpoint) / 1000 >= 1 and len(self.food) < 80:
			self.runtime_checkpoint = self.runtime
			self.food.append(Food(self, self._random_pos()))

		# Move all animals
		for rabbit in self.rabbits:
			rabbit.move()
		for wolf in self.wolves:
			wolf.move()
		
		# Stop condition
		if self._end_condition():
			self.running = False
			return

		# Redraw all entities
		self._update_screen()
		
	def _update_screen(self) -> None:
		"""
		Draws all entities in the world to the screen
		"""

		for rabbit in self.rabbits:
			rabbit.draw(self.screen)

		for wolf in self.wolves:
			wolf.draw(self.screen)

		for food in self.food:
			food.draw(self.screen)
		
	def in_bounds(self, pos: (float, float)) -> bool:
		"""
		Determines if a position is valid in the world

		Args:
			pos ( (float, float) ): Position

		Returns:
			bool: True if pos is valid in the world, False otherwise
		"""
		
		return (
			0 <= pos[0] < self.size[0] and
			0 <= pos[1] < self.size[1]
			)

	def _end_condition(self) -> bool:
		"""
		Determines if the simulation is completed

		Returns:
			bool: True if the world is "complete", False otherwise
		"""

		return len(self.rabbits) <= 1 or len(self.wolves) <= 0
		# return len(self.rabbits) <= 0 or len(self.wolves) <= 0

	def _random_pos(self) -> (float, float):
		"""
		Returns a random position in the world

		Args:
			self (World): self

		Returns:
			(float, float): Tuple representing the position
		"""
		
		return (
			random.uniform(0, self.size[0]),
			random.uniform(0, self.size[1])
			)

	def __repr__(self) -> str:
		return "size={}, rabbits={}, wolves={}, food={}".format(
			self.size,
			len(self.rabbits),
			len(self.wolves),
			len(self.food)
		)