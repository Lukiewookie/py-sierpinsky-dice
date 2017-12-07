#!/usr/bin/python3

import random

import pygame
from pygame import gfxdraw

pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("py-sierpinski-dice")

x = {'1': 10, '2': 360, '3': 710}  # TODO: Automatically calculate the point positions
y = {'1': 606, '2': 10, '3': 606}

red = (250, 0, 0)
green = (0, 250, 0)

font = pygame.font.SysFont("monospace", 16)

pygame.gfxdraw.pixel(screen, x['1'], y['1'], red)
pygame.gfxdraw.pixel(screen, x['2'], y['2'], red)
pygame.gfxdraw.pixel(screen, x['3'], y['3'], red)

rand_x = random.randint(x['1'], x['3'])
rand_y = random.randint(y['1'], y['3'])
pygame.gfxdraw.pixel(screen, rand_x, rand_y, green)

pygame.display.update()


def drawer(gen_x, gen_y):
    iteration = 0
    while True:

        iteration += 1

        dice = str(random.randint(1, 3))

        gen_x = (gen_x + x[dice]) / 2
        gen_y = (gen_y + y[dice]) / 2

        label = font.render("Iteration: %s" % str(iteration), False, (255, 255, 255), (0, 0, 0))
        screen.blit(label, (600, 50))

        pygame.gfxdraw.pixel(screen, int(gen_x), int(gen_y), green)
        pygame.display.update()

# TODO: Calculate the number of iterations etc.

if __name__ == '__main__':
    generated_points = drawer(rand_x, rand_y)
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit(0)
