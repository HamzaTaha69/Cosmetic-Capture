import time

import random

import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 1000, 1000

BLUE = 0, 125, 250
GREEN = 0, 200, 0
BLACK = 0, 0, 0
RED = 250, 0, 0

SCORE = 0 

TIMER = 60

start = False

x = WIDTH / 2 - 40
y = HEIGHT - 100

xs = 80
ys = 40

FT = 1

VEL = 3

D = "EASY"

FPS = 60

DIFFICULTYSET = False

caption = "Cosmetic Capture"

RFX = random.randint(0, WIDTH)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(caption)

pb = pygame.image.load("button.png")
pb = pygame.transform.scale(pb, (150, 150))

pbr = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 2 - 20, 150, 80)

MCR = pygame.Rect(0, 0, 10, 10)

db = pygame.image.load("diffculty button.png")
db = pygame.transform.scale(db, (150, 150))

easy = pygame.image.load("easy.png")

easy_rect = pygame.Rect(WIDTH / 2 - 45, HEIGHT / 2 + 145, 100, 50)

hard = pygame.image.load("hard.png")

hard_rect = pygame.Rect(WIDTH / 2 - 45, HEIGHT / 2 + 200, 100, 50)

dbr = pygame.Rect(WIDTH / 2 - 75, 580, 150, 60)

bg = pygame.image.load("SKYY.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

sbg = pygame.image.load("sbg.png")
sbg = pygame.transform.scale(sbg, (WIDTH, HEIGHT))

food1 = pygame.image.load("banana.png")
food1 = pygame.transform.scale(food1, (150, 150))

food1hit = food1.get_rect()

player = pygame.Rect(x, y, xs, ys)

ply_img = pygame.image.load("bowl.png")
ply_img = pygame.transform.scale(ply_img, ((xs + 70), (ys + 110)))

def CRS():
    MX, MY = pygame.mouse.get_pos()
    MCR.x = MX
    MCR.y = MY
    
def draw_difficulty():
    screen.blit(easy, (WIDTH / 2 - 45, HEIGHT / 2 + 120))
    screen.blit(hard, (WIDTH / 2 - 45, HEIGHT / 2 + 180))
    pygame.display.update()

def draw_start():
    screen.fill(BLUE)
    screen.blit(sbg, (0, 0))
    screen.blit(pb, (WIDTH / 2 - 75, HEIGHT / 2 - 40))
    screen.blit(db, (WIDTH / 2 - 75, HEIGHT / 2 + 40))
    pygame.display.update()
    
def start_game():
    global draw_game
    def draw_game():
        screen.fill(BLUE)
        screen.blit(bg, (0, 0))
        screen.blit(ply_img, (player.x - 35, player.y - 50))
        pygame.display.update()
        
    font = pygame.font.SysFont(None, 35)
        
    def MTS(msg, color):
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text, (100, 50))
        screen_text = font.render(str(SCORE), True, color)
        screen.blit(screen_text, (200, 50))
        screen_text = font.render("TIMER: ", True, color)
        screen.blit(screen_text, (WIDTH - 200, 50))
        screen_text = font.render(str(round(TIMER)), True, color)
        screen.blit(screen_text, (WIDTH - 100, 50))
        pygame.display.update()
        
    def movement():
        global player
        global x
        global y
        global xs
        global ys
        mx, my = pygame.mouse.get_pos()
        x = mx
        y = HEIGHT - 100
                
        player.x = x
        player.y = y

    def timer():
        global TIMER
        TIMER -= 0.025
        items()
        MTS("SCORE: ", BLACK)
        
    def items():
        global food1
        global RFX
        global SCORE
        global ys
        global xs
        global player
        global ply_img
        global FT
        
        if D == "EASY":
            VEL = 4
        
        if D == "HARD":
            VEL = 20
        
        food1hit.y += VEL
        if food1hit.y > HEIGHT:
            food1hit.y = 0
            RFX = random.randint(50, WIDTH - 50)
            food1hit.x = RFX
            if random.randint(1, 3) == 1:
                FT = 1
                food1 = pygame.image.load("banana.png")
            if random.randint(1, 3) == 2:
                FT = 2
                food1 = pygame.image.load("taco.png")
            if random.randint(1, 3) == 3:
                FT = 3
                food1 = pygame.image.load("carrot.png")
                
        food1 = pygame.transform.scale(food1, (150, 150))
                
        screen.blit(food1, (food1hit.x, food1hit.y))
        pygame.display.update()
            
        if player.colliderect(food1hit):
            if FT == 1:
                SCORE += 1
                xs += 1
                ys += 1
            
            if FT == 2:
                SCORE += 2
                xs += 2
                ys += 2
                
            if FT == 3:
                SCORE += 3
                xs += 3
                ys += 3
                
            food1hit.y = 0
            RFX = random.randint(50, WIDTH - 50)
            food1hit.x = RFX
            if random.randint(1, 3) == 1:
                FT = 1
                food1 = pygame.image.load("banana.png")
            if random.randint(1, 3) == 2:
                FT = 2
                food1 = pygame.image.load("taco.png")
            if random.randint(1, 3) == 3:
                FT = 3
                food1 = pygame.image.load("carrot.png")
            
    MTS("SCORE: ", BLACK)
        
    draw_game()
    
    timer()
    
    movement()
    
    items()
    
DFONT = pygame.font.SysFont(None, 100)
    
def DMTS(msgg, color, color2):
    DT = DFONT.render (msgg, True, color)
    screen.blit(DT, (50, 100))
    DT = DFONT.render (str(SCORE), True, color2)
    screen.blit(DT, (WIDTH / 2 + 15, 170))
    pygame.display.flip()
    
def draw_difficulty():
    screen.blit(easy, (WIDTH / 2 - 45, HEIGHT / 2 + 120))
    screen.blit(hard, (WIDTH / 2 - 45, HEIGHT / 2 + 180))
    pygame.display.update()
    
def draw_difficulty2():
    screen.blit(easy, (WIDTH / 2 - 45, HEIGHT / 2 + 120))
    screen.blit(hard, (WIDTH / 2 - 45, HEIGHT / 2 + 180))
    pygame.display.update()

def main_loop():
    global D
    global DIFFICULTYSET
    global TIMER
    global start
    clock = pygame.time.Clock()
    run = True
    while run == True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False 
                 
            if e.type == pygame.MOUSEBUTTONDOWN:
                if MCR.colliderect(pbr):
                    start = True
                    DIFFICULTYSET = False
                    
            if e.type == pygame.MOUSEBUTTONDOWN:
                if MCR.colliderect(dbr):
                    DIFFICULTYSET = True
                    
            if e.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.colliderect(MCR):
                    D = "EASY"
                    start = True
                    TIMER = 45
                    DIFFICULTYSET = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if hard_rect.colliderect(MCR):
                    D = "HARD"
                    start = True
                    TIMER = 25
                    DIFFICULTYSET = False
                
        if start == False: 
            draw_start()
        else:
            start_game()
            
        if DIFFICULTYSET == True:
            draw_difficulty2()
            draw_difficulty()
            
        if TIMER < 0:
            DMTS("YOUR FINAL SCORE WAS: ", BLACK, RED)
            time.sleep(2)
            start = False
            TIMER = 60
        
        CRS()
                
    pygame.quit()
    
if __name__ == "__main__":
    
    main_loop()