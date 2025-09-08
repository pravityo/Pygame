# python
import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot

print("Player loaded. Base:", CircleShape, "module:", CircleShape.__module__)

class Player(CircleShape):
   def __init__(self, x, y, shots):
      super().__init__(x, y, PLAYER_RADIUS)
      self.rotation = 0
      self.timer = 0
      self.shots = shots

   # in the player class
   def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]

   # overriding triangle shape
   def draw(self, screen):
      pygame.draw.polygon(screen, "white", self.triangle(), 2)

   # allow rotation
   def rotate(self, dt):
      self.rotation += PLAYER_TURN_SPEED * dt

   def update(self, dt):
      keys = pygame.key.get_pressed()
      self.timer = max(0, self.timer - dt)
      if keys[pygame.K_a]:
         self.rotate(-dt)
      if keys[pygame.K_d]:
         self.rotate(dt)
      if keys[pygame.K_w]:
         self.move(dt)
      if keys[pygame.K_s]:
         self.move(-dt)
      if keys[pygame.K_SPACE] and self.timer <= 0:
         self.shoot()
      

   #allow forward and backward movement
   def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt


   def shoot(self):
      x, y = self.position.x, self.position.y
      shot = Shot(x, y)
      self.timer = PLAYER_SHOOT_COOLDOWN
      direction = pygame.Vector2(0, 1).rotate(self.rotation)
      shot.velocity = direction * PLAYER_SHOOT_SPEED
      self.shots.add(shot)
