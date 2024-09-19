import pygame

from pygame.locals import *
from random import randint
from sys import exit

pygame.init()

scale = 2
width = 540 * scale
height = 280 * scale

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

        if self.x > width - self.x/4.5:
            self.x -= x

        if self.x < 0:
            self.x -= x

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 200, 20))

class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 10)

x = (width / 2) - (200 / 2)
y = 0

player = player(x, y)
ball = ball(width / 2, height / 2)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.fill((0, 0 ,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_a]:
            player.move(-10, 0)
        elif pygame.key.get_pressed()[K_d]:
            player.move(10, 0)

    player.draw()
    ball.draw()
    pygame.display.update()