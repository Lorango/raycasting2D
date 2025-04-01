#!/usr/bin/python

import math
import pygame
from pygame.locals import *

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption('Svitlo')

clock = pygame.time.Clock()
time = clock.tick()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

poligon_0 = ((200, 100), (100, 200), (50, 150))
poligon_1 = ((500, 400), (580, 320), (650, 420))
poligon_2 = ((410, 120), (500, 120), (510, 220), (420, 220))
poligon_3 = ((100, 300), (200, 300), (200, 400), (100, 400))
poligon_4 = ((50, 50), (750, 50), (750, 430), (50, 430))
poligon_5 = ((300, 300), (310, 300), (310, 310), (300, 310))
poligon_6 = ((320, 300), (330, 300), (330, 310), (320, 310))
poligon_7 = ((700, 70), (690, 110), (730, 120), (710, 170), (600, 200))
poligoni = (poligon_4, poligon_1, poligon_2, poligon_3, poligon_0, poligon_5, poligon_6, poligon_7)

kuti = [0, 120, 240]
poz = [300, 120]

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pass
    screen.fill((10,100,10))
    poz = pygame.mouse.get_pos()
    
## određivanje zraka
    zrake = []
    for poligon in poligoni:
        pygame.draw.polygon(screen, black, poligon, 0)
        pygame.draw.polygon(screen, red, poligon, 2)
        for i, tocka in enumerate(poligon):
            dx_z = tocka[0] - poz[0] # delta X
            dy_z = tocka[1] - poz[1] # delta y
            kut_z = math.atan2(dy_z, dx_z) # kut_z
            zrake.append(kut_z-0.001)
            zrake.append(kut_z)
            zrake.append(kut_z+0.001)

## izracun
    poli = []
    for zraka in zrake:
        parametri = []
        for poligon in poligoni:
            for i, tocka in enumerate(poligon):
                x_s1, y_s1 = poligon[i-1] # x_0, <_0
                dx_s = tocka[0] - x_s1 # delta X
                dy_s = tocka[1] - y_s1 # delta y

                x_z1, y_z1 = poz # x_1, y_1
                dx_z = 100*math.cos(zraka)# delta X
                dy_z = 100*math.sin(zraka)# delta y

                kut_s = math.atan2(dy_s, dx_s)
                kut_z = zraka
                
                if kut_s < 0:
                    kut_s += math.pi
                elif kut_s >= math.pi:
                    kut_s -= math.pi

                if kut_z < 0:
                    kut_z += math.pi
                elif kut_z >= math.pi:
                    kut_z -= math.pi

                kut_s = math.ceil(kut_s*1000)
                kut_z = math.ceil(kut_z*1000)

                if kut_s != kut_z:
                    t_z = (dx_s*(y_z1-y_s1)-dy_s*(x_z1-x_s1)) / (dy_s*dx_z - dx_s*dy_z)
                    if dx_s != 0:
                        t_s = (dx_z*t_z + x_z1-x_s1) / (dx_s)
                    else:
                        t_s = (dy_z*t_z + y_z1-y_s1) / (dy_s)
                        
                    x = math.ceil(dx_s*t_s + x_s1)
                    y = math.ceil(dy_s*t_s + y_s1)
                    
                    if t_z >= 0 and t_s <= 1 and t_s >= 0:
                        parametri.append((t_z, [x, y], zraka))

        parametri.sort(key=lambda tup: tup[0])
        for j, parametar in enumerate(parametri):
            if j != 0:
##                pygame.draw.circle(screen, green, parametar[1], 3, 0)
                pass
            else:
##                pygame.draw.circle(screen, red, parametar[1], 3, 0)
##                pygame.draw.line(screen, red, poz, parametar[1], 1)
                poli.append(parametar[1:])
                
#### sortiranje pp prema kut između pojedine točke pp i poz
    poli.sort(key=lambda tup: tup[1])
    poli_ = []
    for p in poli:
        poli_.append(p[0])

    pygame.draw.polygon(screen, white, poli_, 0)
##    pygame.draw.polygon(screen, [200, 150, 100], poli_, 2)
    pygame.draw.circle(screen, black, poz, 10, 1)
    pygame.display.flip()
