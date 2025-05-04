import pygame
from constants import *
from player import *


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
        screen.fill("black")

        # draw player
        player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player_1.draw(screen)
        

        pygame.display.flip()

        clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    # fill the screen with a color to wipe away anything from last frame


if __name__ == "__main__":
    main()