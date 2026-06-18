import pygame
from abc import ABC, abstractmethod

from code.Const import ENTITY_HEALTH, ENTITY_SPEED

class Entity(ABC, pygame.sprite.Sprite):
  def __init__(self, name: str, position: tuple, animations: dict ):
    super().__init__()
    self.name = name
    self.position = position
    self.speed = ENTITY_SPEED[self.name]
    self.health = ENTITY_HEALTH[self.name]
    self.animations = animations
    self.image = None
    self.rect = None
  
  @abstractmethod
  def update(self): #engloba todas as ações físicas dos frames
    pass