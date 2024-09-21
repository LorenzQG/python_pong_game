import pygame
import math

from pygame.locals import *
from random import randrange
from sys import exit

pygame.init()

scale = 2
width = 540 * scale
height = 280 * scale

class player:
    height = 20
    width = 200
    score = 0

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
        draw = pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        return draw

class enemy:
    height = 20
    width = 200
    speed = 2
    score = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):

        if self.x + self.width / 2 < ball.x:
            self.x += self.speed
        elif self.x + self.width / 2 > ball.x:
            self.x -= self.speed

        if self.x > width - self.width:
            self.x = width - self.width

        if self.x < 0:
            self.x = 0

    def draw(self):
        draw = pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
        return draw
class ball:

    x = 0
    y = 0
    speed = 2
    angle = randrange(120 - 45) + 46
    radius = 10

    dy = math.sin(math.radians(angle)) * speed
    dx = math.cos(math.radians(angle)) * speed

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        if self.x > width - 10:
            self.dx *= -1

        if self.x < 0:
            self.dx *= -1

        if self.y > height + 10:
            player.score += 1
            self.x = width / 2
            self.y = height / 2
            self.angle = randrange(120 - 45) + 46
            self.dy = math.sin(math.radians(self.angle)) * self.speed
            self.dx = math.cos(math.radians(self.angle)) * self.speed
        
        if self.y < 0:
            enemy.score += 1
            self.x = width / 2
            self.y = height / 2
            self.angle = randrange(120 - 45) + 46
            self.dy = math.sin(math.radians(self.angle)) * self.speed
            self.dx = math.cos(math.radians(self.angle)) * self.speed

        if self.y < player.height + self.radius and self.x > player.x and self.x < player.x + player.width:
            self.dy *= -1

        if self.y > enemy.y - self.radius and self.x > enemy.x and self.x < enemy.x + enemy.width:
            self.dy *= -1

    def draw(self):
        draw = pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.radius)
        return draw
        

x = (width / 2) - (200 / 2)
y = 0

player = player(x, y)
enemy = enemy(x, height - 20)
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
    enemy.draw()
    ball.draw()
    ball.move()
    enemy.move()

    pygame.display.update()