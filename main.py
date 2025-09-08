# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
print("Using Player from", Player.__module__, "MRO:", Player.__mro__)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

def main():
   pygame.init()
   print("Starting Asteroids!")
   print("Screen width:", SCREEN_WIDTH)
   print("Screen height:", SCREEN_HEIGHT)
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()

   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
   
   AsteroidField()

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            return
      
      screen.fill((0, 0, 0))
      for sprite in drawable:
         sprite.draw(screen)
      pygame.display.flip()

      dt = clock.tick(60) / 1000
      updatable.update(dt)

      for asteroid in asteroids:
         for shot in shots:
            if asteroid.collision(shot): 
               shot.kill()
               asteroid.split()
         if asteroid.collision(player):
            print("Game over!")
            sys.exit()

if __name__ == "__main__":
    main()
