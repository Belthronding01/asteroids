import pygame
import constants

def main():
	pygame.init()
	print("Starting asteroids!")
	SCREEN_WIDTH = constants.SCREEN_WIDTH
	SCREEN_HEIGHT = constants.SCREEN_HEIGHT
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for	event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")
		
		pygame.display.flip()
	

if __name__ == "__main__":
    main()