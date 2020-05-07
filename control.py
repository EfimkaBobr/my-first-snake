import pygame
from pygame.locals import *


class Control:

    def __init__(self):
        self.flag_game = True
        self.direction = "UP"

        self.right = True
        self.left = True
        self.up = True
        self.down = False

    def control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_game = False
            elif event.type == KEYDOWN:
                if event.key == K_UP and self.up:
                    self.direction = "UP"
                    self.right = True
                    self.left = True
                    self.down = False
                if event.key == K_DOWN and self.down:
                    self.direction = "DOWN"
                    self.right = True
                    self.left = True
                    self.up = False
                if event.key == K_RIGHT and self.right:
                    self.direction = "RIGHT"
                    self.up = True
                    self.down = True
                    self.left = False
                if event.key == K_LEFT and self.left:
                    self.direction = "LEFT"
                    self.up = True
                    self.down = True
                    self.right = False
