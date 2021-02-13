import pygame
from worldtools import *
from animal import State, Animal

from math import sin, cos, pi
from random import uniform

WOLF_IMAGE = pygame.image.load("./img/wolf.png")
WOLF_SIZE = 30
WOLF_IMAGE = pygame.transform.scale(WOLF_IMAGE, (WOLF_SIZE, WOLF_SIZE))


class Wolf(Animal):
	def __init__(self, world, pos: (int, int), speed: float):
		Animal.__init__(self, world, pos, speed)
		self.sight = 200


	def move(self):
		foodlist, rabbitlist, wolflist = self.sight_entities()

		if self.state == State.ROAM or self.hunger <= 50:
			# If a rabbit is in sight / Find closest target
			if rabbitlist:
				self.target = rabbitlist[0]
			# Make a random movement towards a direction

			if (self.target is not None) and (self.target in self.world.rabbits):
				dist_to_target = distance(self.pos, self.target.pos)

				if dist_to_target <= self.speed:
					self.pos = self.target.pos
					self.world.rabbits.remove(self.target)
					self.target = None
				
					self.eat(30)
					if self.eat_count % 3 == 0 and self.eat_count != self._food_checkpoint:
						self._food_checkpoint_checkpoint = self.eat_count
						self.state = State.REPRODUCE
				else:
					ratio = self.speed / dist_to_target
					self.pos = (
						self.pos[0] + ((self.target.pos[0] - self.pos[0]) * ratio),
						self.pos[1] + ((self.target.pos[1] - self.pos[1]) * ratio)
					)
			else:
				self.roam_move()
		elif self.state == State.REPRODUCE:
			if wolflist:
				for w in wolflist:
					if w.state == State.REPRODUCE:
						self.target = w
						break
			
			if (self.target is not None) and (self.target in self.world.wolves):
				dist_to_target = distance(self.pos, self.target.pos)

				# If wolf can jump directly to partner
				if dist_to_target <= self.speed:
					self.pos = self.target.pos
					self.world.wolves.append(Wolf(self.world, self.pos, variance(self.speed, self.target.speed, 1.0)))
					
					self.state = State.ROAM
					self.target.state = State.ROAM

					self.target = None
				else:
					ratio = self.speed / dist_to_target
					self.pos = (
						self.pos[0] + ((self.target.pos[0] - self.pos[0]) * ratio),
						self.pos[1] + ((self.target.pos[1] - self.pos[1]) * ratio)
						)
			else:
				self.roam_move()
		
		# Calculate hunger after movement
		self.hunger -= 0.25
		if self.hunger <= 0:
			self.world.wolves.remove(self)

	def draw(self, screen: pygame.Surface):
		screen.blit(WOLF_IMAGE, (self.pos[0] - WOLF_SIZE/2, self.pos[1] - WOLF_SIZE/2))