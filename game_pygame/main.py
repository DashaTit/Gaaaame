import pygame, controls
from cat import Cat
from pygame.sprite import Group
from stats import Stats


def run():
  pygame.init()
  screen = pygame.display.set_mode((700, 600))
  pygame.display.set_caption("gaaaame")
  bg_color = (250, 218, 221)
  cat = Cat(screen)
  bullets = Group()
  fishes = Group()
  controls.create_army(screen, fishes)
  stats = Stats()



  while True:
    controls.events(screen, cat, bullets)
    cat.update_cat()
    controls.update(bg_color, screen, cat, fishes, bullets)
    controls.update_bullets(fishes, bullets)
    controls.update_fish(stats, screen, cat, fishes, bullets)

run()