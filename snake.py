from settings import *


class Snake:

    def __init__(self):
        self.len = 1
        self.head_x = SNAKE_H_X
        self.head_y = SNAKE_H_Y
        self.snake = [(self.head_x, self.head_y)]

    def save_snake_pos(self):
        if len(self.snake) == self.len:
            self.snake.pop(0)
        self.snake.append((self.head_x, self.head_y))

    def check_pos(self, control):
        if self.head_y < 0 or self.head_y >= SCREEN_SIZE[1] - SNAKE_HEIGHT:
            control.flag_game = False
        elif self.head_x < 0 or self.head_x >= SCREEN_SIZE[0] - SNAKE_WIDTH:
            control.flag_game = False

    def move(self, control):
        if control.direction == "UP":
            self.save_snake_pos()
            self.head_y -= SNAKE_SPEED

        elif control.direction == "DOWN":
            self.save_snake_pos()
            self.head_y += SNAKE_SPEED

        elif control.direction == "RIGHT":
            self.save_snake_pos()
            self.head_x += SNAKE_SPEED

        elif control.direction == "LEFT":
            self.save_snake_pos()
            self.head_x -= SNAKE_SPEED
