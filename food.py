import random

from settings import *


class Food:
    def __init__(self):
        self.food = []

    def create_food(self):
        if len(self.food) == 0:
            for _ in range(0, random.randint(0, MAX_FOOD)):
                self.food.append((random.randint(0, SCREEN_SIZE[0] - FOOD_WIDTH),
                                  random.randint(0, SCREEN_SIZE[1] - FOOD_HEIGHT)))

    def check_food(self, cords_snake):
        for f_cord in self.food:
            if f_cord[0] <= cords_snake[0] + SNAKE_WIDTH // 2 <= f_cord[0] + FOOD_WIDTH and f_cord[1] <= cords_snake[
                1] + \
                    SNAKE_HEIGHT // 2 <= f_cord[1] + FOOD_HEIGHT:
                self.food.remove(f_cord)
                return True
