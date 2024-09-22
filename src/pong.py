import pygame
import math
import random

from pygame.locals import *
from random import randrange
from sys import exit

pygame.init()

scale = 2
width = 540 * scale
height = 280 * scale
isRunning = True

def restart():
    player.score = 0
    enemy.score = 0
    player.x = (width / 2) - (200 / 2)
    player.y = 0
    enemy.x = (width / 2) - (200 / 2)
    enemy.y = height - 20
    ball.x = width / 2
    ball.y = height / 2
    ball.angle = randrange(120 - 45) + 46
    ball.dy = math.sin(math.radians(ball.angle)) * ball.speed
    ball.dx = math.cos(math.radians(ball.angle)) * ball.speed

def show_text(text, size, color, x, y):
    fonte = pygame.font.SysFont('arial', size, True, True)
    text = fonte.render(text, True, color)
    textRect = text.get_rect()
    textRect.midtop = (x, y)
    screen.blit(text, textRect)

def show_screen():
    show_text('Pong', 60, (255, 255, 255), width / 2, 50)
    show_text('Press Space to play', 30, (255, 255, 255), width / 2, height / 2)
    show_text('Press ESC to exit', 30, (255, 255, 255), width / 2, height / 2 + 50)
    show_text('Use A and D to move', 30, (255, 255, 255), width / 2, height / 2 + 100)
    pygame.display.flip()

    waitForPlayer()

def show_game_over():
    show_text('Game Over', 60, (255, 255, 255), width / 2, 50)
    show_text('Press Space to play again', 30, (255, 255, 255), width / 2, height / 2)
    show_text('Press ESC to exit', 30, (255, 255, 255), width / 2, height / 2 + 50)
    pygame.display.flip()

    waitForPlayer()

def waitForPlayer():
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                waiting = False
                isRunning = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def putName():
    insertName = input("Digite seu nome: ").upper()
    if len(insertName) > 3 or len(insertName) < 3:
        print("Digite um nome com 3 caracteres")
        return putName()
    else:
        player.insertName(insertName)
class player:
    height = 20
    width = 200
    score = 0
    name = ""

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
    
    def insertName(self, name):
        self.name = name

class enemy:
    height = 20
    width = 200
    speed = 3
    score = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        target_x = ball.x + random.uniform(-50, 100)

        if self.x + self.width / 2 < target_x:
            self.x += self.speed * 0.7
        elif self.x + self.width / 2 > target_x:
            self.x -= self.speed * 0.7

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
            pointSound.play()
            self.x = width / 2
            self.y = height / 2
            self.angle = randrange(120 - 45) + 46
            self.dy = math.sin(math.radians(self.angle)) * self.speed
            self.dx = math.cos(math.radians(self.angle)) * self.speed
        
        if self.y < 0:
            enemy.score += 1
            pointSound.play()
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

putName()

screen = pygame.display.set_mode((width, height))
fonte = pygame.font.SysFont('arial', 40, True, True)
pygame.display.set_caption('Pong')

pygame.mixer.music.set_volume(0.2)
backgroundSound = pygame.mixer.music.load("./sounds/John Lopker - I'm a Swifty Now _ Taylor Swift Fan Song.mp3")
pygame.mixer.music.play(-1)

pointSound = pygame.mixer.Sound("./sounds/smw_coin.wav")
pointSound.set_volume(0.9)

gameOverSound = pygame.mixer.Sound("./sounds/smw_game_over.wav")                   
gameOverSound.set_volume(0.9)

clock = pygame.time.Clock()

show_screen()

while isRunning:
    clock.tick(60)
    screen.fill((0, 0 ,0))
    enemyMessage = fonte.render(str(enemy.score), True, (255, 255, 255))
    enemyName = fonte.render('ENM', True, (255, 255, 255))
    playerMessage = fonte.render(str(player.score), True, (255, 255, 255))
    playerName = fonte.render(player.name, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_a]:
            player.move(-10, 0)
        elif pygame.key.get_pressed()[K_d]:
            player.move(10, 0)

    if enemy.score == 5:
        pygame.mixer.music.stop()
        gameOverSound.play()
        show_game_over()
        restart()

    pygame.draw.line(screen, (255, 255, 255), (0, height / 2), (width, height / 2))
    screen.blit(enemyMessage, (width - 50, height / 2 + 25))
    screen.blit(enemyName, (width - 170, height / 2 + 25))
    screen.blit(playerMessage, (width - 50, height / 2 - 50))
    screen.blit(playerName, (width - 170, height / 2 - 50))
    player.draw()
    enemy.draw()
    ball.draw()
    ball.move()
    enemy.move()

    pygame.display.update()