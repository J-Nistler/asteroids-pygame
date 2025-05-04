import pygame
from constants import *



def main ():
    pygame.init()
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # infinite game loop
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()