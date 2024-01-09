import pygame, sys
from bullet import Bullet
from fish import Fish
import time

def events(screen, cat, bullets):
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_d:
            cat.mright = True
          elif event.key == pygame.K_a:
            cat.mleft = True
          elif event.key == pygame.K_SPACE:
              new_bullet = Bullet(screen, cat)
              bullets.add(new_bullet)
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_d:
              cat.mright = False
          elif event.key == pygame.K_a:
              cat.mleft = False

def update(bg_color, screen, cat, fishes, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cat.output()
    fishes.draw(screen)
    pygame.display.flip()

def update_bullets(fishes, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
          bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, fishes, True, True)

def update_fish(stats, screen, cat, fishes, bullets):
    fishes.update()
    if pygame.sprite.spritecollideany(cat, fishes):
        cat_kill(stats, screen, cat, fishes, bullets)


def create_army(screen, fishes):
    fish = Fish(screen)
    fish_width = fish.rect.width
    number_fish_x = int((700 - 2 * fish_width) / fish_width)
    fish_height = fish.rect.height
    number_fish_y = int((600 - 100 - 2*fish_height) / fish_height)

    for row in range(number_fish_y - 1):
        for fish_number in range(number_fish_x):
            fish = Fish(screen)
            fish.x = fish_width + fish_width * fish_number
            fish.y = fish_height + fish_height * row
            fish.rect.x = fish.x
            fish.rect.y = fish.rect.height + fish.rect.height * row
            fishes.add(fish)



def cat_kill(stats, screen, cat, fishes, bullets):
    stats.cats_left -= 1
    fishes.empty()
    bullets.empty()
    create_army(screen, fishes)
    cat.create_cat()
    time.sleep(2)