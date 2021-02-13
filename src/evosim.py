import sys
import pygame
from world import World
from simstats import StatClump

import matplotlib.pyplot as plt

DEFAULT_SCREEN_SIZE = (800, 600)
# DEFAULT_SCREEN_SIZE = (1280, 720)
# BG_IMG = pygame.image.load("./img/bg.jpg")

if __name__ == "__main__":
	# Start pygame
	pygame.init()

	# pygame screen and timer
	screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE)
	clock = pygame.time.Clock()

	# Create world
	world = World(DEFAULT_SCREEN_SIZE, clock, screen)
	paused = False

	# Create Trackers 
	sc = StatClump(world)
	sc.start_all()

	# Main pygame loop
	while 1:
		# Pause check
		if not paused:
			world.step()
			pygame.display.flip()
			screen.fill((0, 0, 0))
			# screen.blit(BG_IMG, [0, 0])

		# pygame event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				world.running = False
				break
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					paused = not paused

		# Exit condition
		if not world.running:
			break

		# FPS control
		clock.tick(30)

	# Exit pygame
	pygame.quit()

	# join all Trackers
	sc.join_all()

	# Create pyplot environment
	fig, axes = plt.subplots(3, 2)
	fig.canvas.set_window_title("Evolution Simulation Results")

	# Place Trackers
	sc.trackers[0].plot(axes[0, 0])	# Rabbit Count
	sc.trackers[1].plot(axes[1, 0])	# Wolf Count
	sc.trackers[2].plot(axes[2, 0])	# Food Count
	sc.trackers[3].plot(axes[0, 1])	# Rabbit Speed
	sc.trackers[4].plot(axes[1, 1]) # Wolf Speed
	fig.delaxes(axes[2, 1])			# Temp delete

	# Show pyplot results
	fig.tight_layout()
	plt.show()

	print("Simulation Finished")
	sys.exit(0)