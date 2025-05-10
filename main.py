import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main ():
    pygame.init()
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield_main = AsteroidField()

    # infinite game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        screen.fill("black")

        # draw player
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    # fill the screen with a color to wipe away anything from last frame


if __name__ == "__main__":
    main()