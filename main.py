import pygame
import random

from abc import ABC

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Slot Machine")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


class Character(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def draw(self):
        pass


class Player(Character):
    def __init__(self, playerImg, x=370, y=400):
        self.x = x
        self.y = y
        self.playerImg = pygame.image.load(playerImg)
        self.playerchange = 5

    def draw(self):
        screen.blit(self.playerImg, (self.x, self.y))


class Rec(Character):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 5)


# Clock
clock = pygame.time.Clock()

# Pages
global pages
pages = 0

# Slot machine
slotImg = pygame.image.load('Slot.png')
symImg = [pygame.image.load('7.png'),
          pygame.image.load('cherry.png'),
          pygame.image.load('banana.png'),
          pygame.image.load('orange.png')]

# Background
bgImg = [pygame.image.load('bg01.png'),
         pygame.image.load('bg02.png'),
         pygame.image.load('bg03.png'),
         pygame.image.load('bg04.png'),
         pygame.image.load('bg05.png')]
bgDelay = 500
bgCount = 5
choosebg = pygame.image.load('choose.png')
Losebg = [pygame.image.load('lose1.png'),
          pygame.image.load('lose2.png'),
          pygame.image.load('lose3.png'),
          pygame.image.load('lose4.png'),
          pygame.image.load('lose5.png')]
global losecount
losecount = 5

# Casino
casinoImg = pygame.image.load('casino.png')

# Player
hair = 0
body = 0
walkCount = 0
left = False
right = False
startmoney = 20000
money = startmoney

# Green hair
GG = Player('char/charGG.png')
GR = Player('char/charGR.png')
GY = Player('char/charGY.png')
GGwalkR = [pygame.image.load('char/charGG.png'),
           pygame.image.load('char/charGGW.png'),
           pygame.image.load('char/charGGW2.png')]
GGwalkL = [pygame.image.load('char/charGGlt.png'),
           pygame.image.load('char/charGGWlt.png'),
           pygame.image.load('char/charGGW2lt.png')]

GRwalkR = [pygame.image.load('char/charGR.png'),
           pygame.image.load('char/charGRW.png'),
           pygame.image.load('char/charGRW2.png')]
GRwalkL = [pygame.image.load('char/charGRlt.png'),
           pygame.image.load('char/charGRWlt.png'),
           pygame.image.load('char/charGRW2lt.png')]

GYwalkR = [pygame.image.load('char/charGY.png'),
           pygame.image.load('char/charGYW.png'),
           pygame.image.load('char/charGYW2.png')]
GYwalkL = [pygame.image.load('char/charGYlt.png'),
           pygame.image.load('char/charGYWlt.png'),
           pygame.image.load('char/charGYW2lt.png')]

# Red hair
RG = Player('char/charRG.png')
RR = Player('char/charRR.png')
RY = Player('char/charRY.png')
RGwalkR = [pygame.image.load('char/charRG.png'),
           pygame.image.load('char/charRGW.png'),
           pygame.image.load('char/charRGW2.png')]
RGwalkL = [pygame.image.load('char/charRGlt.png'),
           pygame.image.load('char/charRGWlt.png'),
           pygame.image.load('char/charRGW2lt.png')]

RRwalkR = [pygame.image.load('char/charRR.png'),
           pygame.image.load('char/charRRW.png'),
           pygame.image.load('char/charRRW2.png')]
RRwalkL = [pygame.image.load('char/charRRlt.png'),
           pygame.image.load('char/charRRWlt.png'),
           pygame.image.load('char/charRRW2lt.png')]

RYwalkR = [pygame.image.load('char/charRY.png'),
           pygame.image.load('char/charRYW.png'),
           pygame.image.load('char/charRYW2.png')]
RYwalkL = [pygame.image.load('char/charRYlt.png'),
           pygame.image.load('char/charRYWlt.png'),
           pygame.image.load('char/charRYW2lt.png')]

# Yellow hair
YG = Player('char/charYG.png')
YR = Player('char/charYR.png')
YY = Player('char/charYY.png')
YGwalkR = [pygame.image.load('char/charYG.png'),
           pygame.image.load('char/charYGW.png'),
           pygame.image.load('char/charYGW2.png')]
YGwalkL = [pygame.image.load('char/charYGlt.png'),
           pygame.image.load('char/charYGWlt.png'),
           pygame.image.load('char/charYGW2lt.png')]

YRwalkR = [pygame.image.load('char/charYR.png'),
           pygame.image.load('char/charYRW.png'),
           pygame.image.load('char/charYRW2.png')]
YRwalkL = [pygame.image.load('char/charYRlt.png'),
           pygame.image.load('char/charYRWlt.png'),
           pygame.image.load('char/charYRW2lt.png')]

YYwalkR = [pygame.image.load('char/charYY.png'),
           pygame.image.load('char/charYYW.png'),
           pygame.image.load('char/charYYW2.png')]
YYwalkL = [pygame.image.load('char/charYYlt.png'),
           pygame.image.load('char/charYYWlt.png'),
           pygame.image.load('char/charYYW2lt.png')]

# Music and Sound
playsound = pygame.mixer.Sound('play.wav')
winsound = pygame.mixer.Sound('win.wav')
losesound = pygame.mixer.Sound('lose.wav')
pygame.mixer.music.load('bgmusic.ogg')
pygame.mixer.music.play(-1)

# Text and Font
pygame.font.init()
myfont = pygame.font.SysFont('Minecraft', 30)
showmoney = myfont.render('MONEY: %d' % money, False, (255, 255, 255))


def mainpagefunc():
    global bgCount
    if bgCount > 124:
        bgCount = 5
    screen.blit(bgImg[bgCount // 25], (0, 0))
    pygame.display.update()
    bgCount += 1


def player(color, colorWL, colorWR):
    global hair
    global body
    global walkCount
    global left
    global right
    global pages
    rectcasino = Rec(250, 190, 300, 50)
    rectblock1 = Rec(0, 0, 100, 300)
    rectblock2 = Rec(0, 0, 80, 320)
    rectblock3 = Rec(700, 0, 100, 300)
    rectblock4 = Rec(720, 0, 80, 320)
    if walkCount + 1 >= 9:
        walkCount = 0
    if left:
        screen.blit(colorWL[walkCount // 3], (color.x, color.y))
        walkCount += 1
    elif right:
        screen.blit(colorWR[walkCount // 3], (color.x, color.y))
        walkCount += 1
    else:
        screen.blit(color.playerImg, (color.x, color.y))

    if keys[pygame.K_LEFT]:
        color.x -= color.playerchange
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        color.x += color.playerchange
        right = True
        left = False
    elif keys[pygame.K_UP]:
        color.y -= color.playerchange
    elif keys[pygame.K_DOWN]:
        color.y += color.playerchange
    else:
        walkCount = 0
    rectchar = Rec(color.x + 20, color.y, 100, 100)
    if rectchar.rect.colliderect(rectcasino):
        pages = 2
    if color.x > 688:
        color.x = 688
    if color.x < -38:
        color.x = -38
    if color.y > 480:
        color.y = 480
    if color.y < 230:
        color.y = 230
    if rectchar.rect.colliderect(rectblock1):
        color.x += 5
    if rectchar.rect.colliderect(rectblock2):
        color.y += 5
    if rectchar.rect.colliderect(rectblock3):
        color.x -= 5
    if rectchar.rect.colliderect(rectblock4):
        color.y += 5


def back(color):
    global pages
    if keys[pygame.K_o]:
        pages = 1
        color.y += 10


global x
x = 0
global y
y = 0
global z
z = 0

running = True
while running:
    showmoney = myfont.render('MONEY: %d' % money, False, (255, 255, 255))
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
    if money < 0:
        pages = 4
    if keys[pygame.K_m]:
        pages = 0
    if pages == 0:
        mainpagefunc()
        if keys[pygame.K_KP_ENTER]:
            pages = 3

    if pages == 1:
        screen.blit(casinoImg, (0, 0))
        screen.blit(showmoney, (620, 10))
        # GG
        if hair == 0 and body == 0:
            player(GG, GGwalkL, GGwalkR)
        elif hair == 0 and body == 1:
            player(GR, GRwalkL, GRwalkR)
        elif hair == 0 and body == 2:
            player(GY, GYwalkL, GYwalkR)
        elif hair == 1 and body == 0:
            player(RG, RGwalkL, RGwalkR)
        elif hair == 1 and body == 1:
            player(RR, RRwalkL, RRwalkR)
        elif hair == 1 and body == 2:
            player(RY, RYwalkL, RYwalkR)
        elif hair == 2 and body == 0:
            player(YG, YGwalkL, YGwalkR)
        elif hair == 2 and body == 1:
            player(YR, YRwalkL, YRwalkR)
        elif hair == 2 and body == 2:
            player(YY, YYwalkL, YYwalkR)
        pygame.display.update()

        if keys[pygame.K_BACKSPACE]:
            pages = 3

    if pages == 2:
        clock.tick(30)
        screen.blit(slotImg, (0, 0))
        buttonUp = False
        if hair == 0 and body == 0:
            back(GG)
        elif hair == 0 and body == 1:
            back(GR)
        elif hair == 0 and body == 2:
            back(GY)
        elif hair == 1 and body == 0:
            back(RG)
        elif hair == 1 and body == 1:
            back(RR)
        elif hair == 1 and body == 2:
            back(RY)
        elif hair == 2 and body == 0:
            back(YG)
        elif hair == 2 and body == 1:
            back(YR)
        elif hair == 2 and body == 2:
            back(YY)
        num = random.randint(0, 3)
        num2 = random.randint(0, 3)
        num3 = random.randint(0, 3)
        if keys[pygame.K_x]:
            playsound.play(1)
            money -= 100
            x = num
            y = num2
            z = num3
            screen.blit(symImg[num], (271, 213))
            screen.blit(symImg[num2], (351, 213))
            screen.blit(symImg[num3], (431, 213))

            if x == 0 and y == 0 and z == 0:
                money += 7777
                winsound.play(1)
            if x == 1 and y == 1 and z == 1:
                money += 100
                winsound.play(1)
            if x == 2 and y == 2 and z == 2:
                money += 1000
                winsound.play(1)
            if x == 3 and y == 3 and z == 3:
                money += 5000
                winsound.play(1)

        screen.blit(symImg[x], (271, 213))
        screen.blit(symImg[y], (351, 213))
        screen.blit(symImg[z], (431, 213))
        screen.blit(showmoney, (620, 10))
        pygame.display.update()

    if pages == 3:
        screen.fill((0, 0, 0))
        screen.blit(choosebg, (0, 0))
        choosehair1 = Rec(168, 245, 100, 30)
        choosehair1.draw()
        choosehair2 = Rec(349, 245, 100, 30)
        choosehair2.draw()
        choosehair3 = Rec(538, 245, 100, 30)
        choosehair3.draw()
        choosebody1 = Rec(168, 490, 100, 30)
        choosebody1.draw()
        choosebody2 = Rec(349, 490, 100, 30)
        choosebody2.draw()
        choosebody3 = Rec(538, 490, 100, 30)
        choosebody3.draw()
        done = Rec(660, 530, 120, 55)
        done.draw()
        mouse = pygame.mouse.get_pos()
        mouserect = Rec(mouse[0], mouse[1], 20, 20)
        clicked = pygame.mouse.get_pressed()
        if mouserect.rect.colliderect(choosehair1) and clicked[0]:
            hair = 0
            pygame.draw.rect(screen, (0, 255, 250), choosehair1, 5)
        elif mouserect.rect.colliderect(choosehair2) and clicked[0]:
            hair = 1
            pygame.draw.rect(screen, (0, 255, 250), choosehair2, 5)
        elif mouserect.rect.colliderect(choosehair3) and clicked[0]:
            hair = 2
            pygame.draw.rect(screen, (0, 255, 250), choosehair3, 5)
        if mouserect.rect.colliderect(choosebody1) and clicked[0]:
            body = 0
            pygame.draw.rect(screen, (0, 255, 250), choosebody1, 5)
        elif mouserect.rect.colliderect(choosebody2) and clicked[0]:
            body = 1
            pygame.draw.rect(screen, (0, 255, 250), choosebody2, 5)
        elif mouserect.rect.colliderect(choosebody3) and clicked[0]:
            body = 2
            pygame.draw.rect(screen, (0, 255, 250), choosebody3, 5)
        if mouserect.rect.colliderect(done) and clicked[0]:
            pages = 1
            pygame.draw.rect(screen, (0, 255, 250), done, 5)
        pygame.display.update()

    if pages == 4:
        losesound.play(1)
        if losecount > 124:
            losecount = 5
        screen.blit(Losebg[losecount // 25], (0, 0))
        pygame.display.update()
        losecount += 1
        if keys[pygame.K_r]:
            pages = 0
            money = startmoney
            hair = 0
            body = 0
