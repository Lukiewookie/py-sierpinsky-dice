#!/usr/bin/python3

import random
import sys
import time

import pygame
from PIL import Image
from pygame import gfxdraw

pygame.init()

win_width = 800
win_height = 700

iterations_input = int(input("How many iterations to generate?"))

screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("py-sierpinski-dice")

x = {'1': 10,
     '2': win_width-90,
     '3': 10,
     '4': win_width-90}
y = {'1': 10,
     '2': 10,
     '3': win_height-10,
     '4': win_height-10}

red = (250, 0, 0)
green = (0, 250, 0)

font = pygame.font.SysFont("monospace", 16)

for c in range (1, 4):
    c = str(c)
    pygame.gfxdraw.pixel(screen, x[c], y[c], red)


rand_x = random.randint(x['1'], x['2'])
rand_y = random.randint(y['1'], y['3'])
pygame.gfxdraw.pixel(screen, rand_x, rand_y, green)

pygame.display.update()


def drawer(gen_x, gen_y):
    iteration = 0
    try:
        while iteration != iterations_input:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    image_saver(iteration)

            iteration += 1

            dice = str(random.randint(1, 4))

            gen_x = (gen_x + x[dice]) / 2
            gen_y = (gen_y + y[dice]) / 2

            label = font.render("N. of points:%s" % str(iteration), False, (255, 255, 255), (0, 0, 0))
            screen.blit(label, (win_width-200, 20))

            pygame.gfxdraw.pixel(screen, int(gen_x), int(gen_y), green)
            pygame.display.update()
    finally:
        time.sleep(10)
        image_saver(iteration)


def image_saver(num):
    data = pygame.image.tostring(screen, 'RGBA')
    img = Image.frombytes('RGBA', (win_width, win_height), data)
    img.save('sqr_%s.png' % str(num), 'PNG')

    pygame.quit()
    sys.exit(0)


if __name__ == '__main__':
    drawer(rand_x, rand_y)
