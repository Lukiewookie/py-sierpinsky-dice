#!/usr/bin/python3

import random
import sys
import time

import pygame
from pygame import gfxdraw

pygame.init()

screen = pygame.display.set_mode((800, 700))

x = {'1': 10, '2': 360, '3': 710}
y = {'1': 606, '2': 10, '3': 606}

red = (250, 0, 0)
green = (0, 250, 0)

pygame.gfxdraw.pixel(screen, x['1'], y['1'], red)
pygame.gfxdraw.pixel(screen, x['2'], y['2'], red)
pygame.gfxdraw.pixel(screen, x['3'], y['3'], red)

rand_x = random.randint(x['1'], x['3'])
rand_y = random.randint(y['1'], y['3'])
pygame.gfxdraw.pixel(screen, rand_x, rand_y, green)


def drawer(gen_x, gen_y):
    try:
        dice = str(random.randint(1, 3))
        # pygame.gfxdraw.pixel(screen, int(gen_x), int(gen_y), green)

        if gen_x >= x[dice]:
            gen_x = (abs(gen_x-x[dice])/2)+x[dice]
        elif gen_x < x[dice]:
            gen_x = (abs(x[dice]-gen_x)/2)+x[dice]

        if gen_y >= y[dice]:
            gen_y = (abs(gen_y-y[dice])/2)+y[dice]
        elif gen_y < y[dice]:
            gen_y = (abs(y[dice]-gen_y)/2)+y[dice]

        pygame.gfxdraw.pixel(screen, int(gen_x), int(gen_y), green)

        pygame.display.update()

        dict_ret = {'x': gen_x, 'y': gen_y}
        return dict_ret

        # drawer(gen_x, gen_y)

    except RecursionError:
        time.sleep(10)
        sys.exit(1)


if __name__ == '__main__':
    generated_points = drawer(rand_x, rand_y)
    while True:
        drawer(generated_points['x'], generated_points['y'])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
