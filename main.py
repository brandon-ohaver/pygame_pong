import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 900))

pygame.display.set_caption("Pygame - Pong Renewed")

while True:
    # Listen for all events currently occurring
    for event in pygame.event.get():
		# Check for a quit event (triggered when the user presses the close button)
        if event.type == pygame.QUIT:
			# Shut down Pygame
            pygame.quit()
			# Exit the system
            sys.exit()

    # Redraw the entire display
    pygame.display.flip()

	# Tick the clock according to the framerate (60)
    clock.tick(60)

	# Get previous time
    previous_time = clock.get_time()

	# Get current FPS (not always exactly 60)
    fps = clock.get_fps()
    print("hello")
