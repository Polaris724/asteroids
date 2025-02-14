import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatables
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    Shot.containers = (updatables, drawables, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for drawable in drawables:
            drawable.draw(screen)
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                print ("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisioncheck(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
