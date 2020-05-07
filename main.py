from control import Control
from food import Food
from settings import *
from snake import Snake

pg.init()
pg.display.set_caption("Snake")
screen = pg.display.set_mode(SCREEN_SIZE)

snake = Snake()
food = Food()
control = Control()
while control.flag_game:
    control.control()

    snake.move(control)
    snake.save_snake_pos()
    for rect_cords in snake.snake:
        pg.draw.rect(screen, SNAKE_COLOR, pg.Rect(rect_cords[0], rect_cords[1], SNAKE_WIDTH, SNAKE_HEIGHT))
    snake.check_pos(control)

    food.create_food()
    for rect_cords in food.food:
        pg.draw.rect(screen, FOOD_COLOR, pg.Rect(rect_cords[0], rect_cords[1], FOOD_WIDTH, FOOD_HEIGHT))

    if food.check_food(snake.snake[-1]):
        snake.len += 1

    pg.display.update()
    screen.fill(BG_COLOR)
    pg.time.delay(10)
