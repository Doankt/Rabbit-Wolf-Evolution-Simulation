from worldtools import *
from enum import Enum
from math import sin, cos, pi
from random import uniform

class State(Enum):
	ROAM = 0
	REPRODUCE = 1

class Animal:
	"""Class representing Animal in the world"""

	def __init__(self, world, pos: (float, float), speed: float):
		"""
		Initializes the Animal

		Args:
			world (World): The world
			pos ( (float, float) ): Starting position
			speed (float): Animal speed
		"""

		self.speed = speed
		self.pos = pos
		self.world = world

		# Movement variables
		self.target = None
		self.movement_angle = uniform(0, pi*2)

		# Food variables
		self.hunger = 100
		self.eat_count = 0
		self._food_checkpoint = 0

		# Set state
		self.state = State.ROAM
	
	def move(self) -> Exception:
		"""
		Moves an animal based on state

		Raises:
			NotImplementedError: Should be overwritten in a derived class

		Returns:
			Exception: Will always raise NotImplementedError if called from Animal class
		"""
		
		raise NotImplementedError()
		
	def draw(self, screen) -> Exception:
		"""
		Draws an animal to the screen

		Args:
			screen (pygame.screen): pygame screen

		Raises:
			NotImplementedError: Should be overwritten in a derived class

		Returns:
			Exception: Will always raise NotImplementedError if called from Animal class
		"""

		raise NotImplementedError()

	def sight_entities(self) -> (["Food"], ["Rabbit"], ["Wolf"]):
		"""
		Returns all entites in vision of the Animal

		Args:
			self (Animal): self

		Returns:
			([Food], [Rabbit], [Wolf]): Returns a 3-tuple with Food, Rabbit, Wolf in vision
		"""

		# Get foods around self
		foodlist = []
		for food in self.world.food:
			if self != food and self._in_sight(food):	foodlist.append(food)

		# Get rabbits around self
		rabbitlist = []
		for rabbit in self.world.rabbits:
			if self != rabbit and self._in_sight(rabbit): rabbitlist.append(rabbit)

		# Get wolves around self
		wolflist = []
		for wolf in self.world.wolves:
			if self != wolf and self._in_sight(wolf):	wolflist.append(wolf)

		# Sort by distance to self
		foodlist.sort(key=lambda x: distance(self.pos, x.pos))
		rabbitlist.sort(key=lambda x: distance(self.pos, x.pos))
		wolflist.sort(key=lambda x: distance(self.pos, x.pos))

		return (foodlist, rabbitlist, wolflist)
	
	def eat(self, inc: float) -> None:
		"""
		Increments eating food source and adds to hunger

		Args:
			inc (int): Amount to increase hunger
		"""

		# Increment eat count
		self.eat_count += 1

		# Limit to 100
		if self.hunger + inc >= 100:
			self.hunger = 100
		else:
			self.hunger += inc
	
	def roam_move(self) -> None:
		"""
		Moves Animal in the direction they are facing and slightly changes movement angle
		"""

		# Proposed move
		new_x = self.pos[0] + (self.speed * cos(self.movement_angle))
		new_y = self.pos[1] + (self.speed * sin(self.movement_angle))

		# Check if valid move
		while not self.world.in_bounds((new_x, new_y)):
			# Reset move
			self.movement_angle += pi/2
			new_x = self.pos[0] + (self.speed * cos(self.movement_angle))
			new_y = self.pos[1] + (self.speed * sin(self.movement_angle))
			
		# Confirm move
		self.pos = (
			new_x,
			new_y
		)

		# Adjust movement angle
		self.movement_angle += uniform(-pi*2 / 36, pi*2 / 36)
		
	def _in_sight(self, entity) -> bool:
		"""
		Returns if an entity (which has a pos) is in sight of the Animal

		Args:
			entity (Animal or Food): Entity to check

		Returns:
			bool: True if entity is in sight, False otherwise
		"""
		
		return distance(self.pos, entity.pos) <= self.sight

	def __repr__(self) -> str:
		return "{}".format(self.pos)
		# return "speed={}, pos={}, hunger={}, state={}".format(
		# 	self.speed,
		# 	self.pos,
		# 	self.hunger,
		# 	self.state
		# )