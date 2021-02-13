from threading import Thread
from time import time, sleep

TRACKER_TIMEOUT = 3

class StatClump:
	def __init__(self, world):
		self.trackers = [
			RabbitCountTracker(world),
			WolfCountTracker(world),
			FoodCountTracker(world),
			RabbitSpeedTracker(world),
			WolfSpeedTracker(world)
		]

	def start_all(self):
		for thread in self.trackers:
			thread.start()
		
	def join_all(self):
		for thread in self.trackers:
			thread.join()

class Tracker(Thread):
	def __init__(self, world, title, ylabel):
		Thread.__init__(self)

		self.world = world
		self.title = title
		self.ylabel = ylabel
		
		self._last_time = time()

		self.x = []
		self.y = []

	def run(self):
		pass

	def _timeout(self):
		return time() - self._last_time > TRACKER_TIMEOUT

	def plot(self, ax):
		ax.set_title(self.title)

		if len(self.x) == 1 or len(self.y) == 1:
			ax.text(0, 0, "NO DATA", ha="center", va="center")
			ax.set_xlim(-1, 1)
			ax.set_ylim(-1, 1)
			return

		ax.set_xlabel("Time (s)")
		ax.set_ylabel(self.ylabel)

		ax.xaxis.grid(True, which="major")
		ax.yaxis.grid(True, which="major")

		ax.plot(self.x, self.y)

class RabbitCountTracker(Tracker):
	def __init__(self, world):
		Tracker.__init__(self, world, "Rabbit Count", "Rabbits")

	def run(self):
		self.x.append(self.world.runtime/1000)
		self.y.append(len(self.world.rabbits))
		last_count = len(self.world.rabbits)

		while self.world.running:
			if len(self.world.rabbits) != last_count or self._timeout():
				self._last_time = time()
				last_count = len(self.world.rabbits)

				self.x.append(self.world.runtime/1000)
				self.y.append(last_count)
			sleep(1)

class FoodCountTracker(Tracker):
	def __init__(self, world):
		Tracker.__init__(self, world, "Food Count", "Food")

	def run(self):
		self.x.append(self.world.runtime / 1000)
		self.y.append(len(self.world.food))
		last_count = len(self.world.food)

		while self.world.running:
			if len(self.world.food) != last_count or self._timeout():
				self._last_time = time()
				last_count = len(self.world.food)

				self.x.append(self.world.runtime/1000)
				self.y.append(len(self.world.food))
			sleep(1)

class WolfCountTracker(Tracker):
	def __init__(self, world):
		Tracker.__init__(self, world, "Wolf Count", "Wolves")

	def run(self):
		self.x.append(self.world.runtime / 1000)
		self.y.append(len(self.world.wolves))
		last_count = len(self.world.wolves)

		while self.world.running:
			if len(self.world.wolves) != last_count or self._timeout():
				self._last_time = time()
				last_count = len(self.world.wolves)

				self.x.append(self.world.runtime/1000)
				self.y.append(len(self.world.wolves))
			sleep(1)

class RabbitSpeedTracker(Tracker):
	def __init__(self, world):
		Tracker.__init__(self, world, "Average Rabbit Speed", "Speed")

	def _average_speed(self):
		return sum([r.speed for r in self.world.rabbits]) / len(self.world.rabbits)

	def run(self):
		self.x.append(self.world.runtime / 1000)
		self.y.append(self._average_speed())
		last_speed = self._average_speed()

		while self.world.running:
			if self._average_speed() != last_speed or self._timeout():
				self._last_time = time()
				last_speed = self._average_speed()

				self.x.append(self.world.runtime/1000)
				self.y.append(last_speed)
			sleep(1)

class WolfSpeedTracker(Tracker):
	def __init__(self, world):
		Tracker.__init__(self, world, "Average Wolf Speed", "Speed")

	def _average_speed(self):
		return sum([w.speed for w in self.world.wolves]) / len(self.world.wolves)

	def run(self):
		self.x.append(self.world.runtime / 1000)
		self.y.append(self._average_speed())
		last_speed = self._average_speed()

		while self.world.running:
			if self._average_speed() != last_speed or self._timeout():
				self._last_time = time()
				last_speed = self._average_speed()

				self.x.append(self.world.runtime/1000)
				self.y.append(last_speed)
			sleep(1)
