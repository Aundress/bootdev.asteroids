# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import random
import pygame
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                return
        for updates in updatable:
            updates.update(dt) #player.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("GAME OVER")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    

        screen.fill("black")
        
        for draw in drawable:
            draw.draw(screen) 

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
