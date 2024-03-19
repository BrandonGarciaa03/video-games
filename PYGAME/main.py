from turtle import width
import pygame

#initial config
pygame.init()

BG_COLOR = (227, 220, 218)

#create a player screen
WIDHT = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("My game")

#main loop
status = True 
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            status = False 


    screen.fill(BG_COLOR)
    pygame.display.flip()

pygame.quit            