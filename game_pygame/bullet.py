import pygame

class Bullet(pygame.sprite.Sprite):
  def __init__(self, screen, cat):
    super(Bullet, self).__init__()
    self.screen = screen
    self.rect = pygame.Rect(0, 0, 10, 12)
    self.color = 128, 128, 128
    self.speed = 1.5
    self.rect.centerx = cat.rect.centerx
    self.rect.top = cat.rect.top
    self.y = float(self.rect.y)

  def update(self):
    self.y -= self.speed
    self.rect.y = self.y
  def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect)
