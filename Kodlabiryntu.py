#import os
import pygame
#import random
import sys
pygame.init()

szerokosc_poczatkowa = 1280#ilość liter na szerokość x 30
wysokosc_poczatkowa = 720#####

class Sciana:
    def __init__(self, pozycja):
        Sciany.append(self)
        self.rect = pygame.Rect(pozycja[0], pozycja[1], 30, 30)

pygame.display.set_caption("Destiny")
game_display = pygame.display.set_mode((szerokosc_poczatkowa,wysokosc_poczatkowa))

Sciany = []


def reinit():

    Supermarket = [
    "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
    "S     S       S     S      S        S     S",
    "S     S       S     S      S        S     S",
    "S     S       S     S      S        S     S",
    "S     S       S     S               S     S",
    "S     S       S     S               S     S",
    "S     S       S     S               S     S",
    "S     S       S     S      S        S     S",
    "S     S       S     S      S        S     S",
    "S     S       S     S      S        S     S",
    "S     S             S      S        S     S",
    "S     S             S      S              S",
    "S     S             S      S              S",
    "S     S       S     S      S              S",
    "S     S       S     S      S        S     S",
    "S     S       S     S      S        S     S",
    "S     S       S     S      S        S     S",
    "S             S     S      S        S     S",
    "S             S     S      S        S     S",
    "S             S     S      S        S     S",
    "S     S       S            S        S     S",
    "S     S       S            S        S     S",
    "S     S       S            S        S     S",
    "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
    ]
    x=0
    y=0
    for rzad in Supermarket:
        for litera in rzad:
            if litera == "S":
                Sciana((x, y))
            elif litera == "":
                pass
            x += 30
        y += 30
        x = 0
#S - ściana
#spacja - puste

reinit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Dzięki za grę! :)")
            sys.exit(0)

    game_display.fill((0,0,0))
    for Sciana in Sciany:
        pygame.draw.rect(game_display, (255,255,255), Sciana.rect)
    pygame.display.flip()

pygame.quit()
quit()
