# фонова музика
from pygame import *
from random import randint
from time import time as timer

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
window.fill(red)

game = True
finish = False
clock = time.Clock()
FPS = 120



class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.x < 400
            self.rect.x += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] self.rect.y< 400
            self.rect.x += self.speed

racket1 = Player("rct1", 30, 200, 4, 50, 150)
racket2 = Player("rct2", 520, 200, 4, 50, 50)
pong = GameSprite("ball", 200, 200, 4, 50, 50)

while game:
  for e in event.get():
    if e.type == QUIT:
      game=False
    
  if finish !=  True:
    racket1.update_l()
    racket2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
