import pygame
from worldtools import *
from animal import State, Animal

from math import sin, cos, atan2, pi
from random import uniform


RABBIT_IMAGE = pygame.image.load("./img/bunny.png")
RABBIT_SIZE = 30
RABBIT_IMAGE = pygame.transform.scale(RABBIT_IMAGE, (RABBIT_SIZE, RABBIT_SIZE))

class Rabbit(Animal):
	def __init__(self, world, pos: (int, int), speed: int):
		Animal.__init__(self, world, pos, speed)
		self.sight = 150

	def move(self) -> None:
		# Generate all entities in sight
		foodlist, rabbitlist, wolflist = self.sight_entities()

		# Check if any Wolves nearby
		if wolflist:
			avgpoint = (
				sum([w.pos[0] for w in wolflist]) / len(wolflist),
				sum([w.pos[1] for w in wolflist]) / len(wolflist)
			)
			t = atan2(avgpoint[1] - self.pos[1], avgpoint[0] - self.pos[0]) + pi
			# d = distance(self.pos, avgpoint)
			new_x = self.pos[0] + (self.speed * cos(t))
			new_y = self.pos[1] + (self.speed * sin(t))

			if not self.world.in_bounds((new_x, new_y)):
				t = atan2(self.world.size[0]/2 - self.pos[1], self.world.size[1]/2 - self.pos[0])
				new_x = self.pos[0] + (self.speed * cos(t))
				new_y = self.pos[1] + (self.speed * sin(t))

			self.pos = (
				new_x,
				new_y
			)



		elif self.state == State.ROAM or self.hunger <= 50:
			# If a food is in sight / Find closest target
			if foodlist:
				self.target = foodlist[0]

			# Move to food if available
			if (self.target is not None) and (self.target in self.world.food):
				dist_to_target = distance(self.pos, self.target.pos)

				# If rabbit can jump directly to food
				if dist_to_target <= self.speed:
					self.pos = self.target.pos
					self.world.food.remove(self.target)
					self.target = None

					self.eat(30)
					if self.eat_count % 2 == 0 and self.eat_count != self._food_checkpoint:
						self._food_checkpoint_checkpoint = self.eat_count
						self.state = State.REPRODUCE
				# If rabbit must take intermediate steps to food
				else:
					ratio = self.speed / dist_to_target
					self.pos = (
						self.pos[0] + ((self.target.pos[0] - self.pos[0]) * ratio),
						self.pos[1] + ((self.target.pos[1] - self.pos[1]) * ratio)
						)
			# Make a random movement towards a direction
			else:
				self.roam_move()
		elif self.state == State.REPRODUCE:

			if rabbitlist:
				for r in rabbitlist:
					if r.state == State.REPRODUCE:
						self.target = r
						break
			
			if (self.target is not None) and (self.target in self.world.rabbits):
				dist_to_target = distance(self.pos, self.target.pos)

				# If rabbit can jump directly to partner
				if dist_to_target <= self.speed:
					self.pos = self.target.pos
					self.world.rabbits.append(Rabbit(self.world, self.pos, variance(self.speed, self.target.speed, 1.0)))
					
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
			self.world.rabbits.remove(self)
				
	def draw(self, screen: pygame.Surface) -> None:
		screen.blit(RABBIT_IMAGE, (self.pos[0] - RABBIT_SIZE/2, self.pos[1] - RABBIT_SIZE/2))
		# pygame.draw.circle(screen, (255, 255, 255), self.pos, 10)