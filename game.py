import pygame
import time
import random

pygame.init()


width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def display_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    win.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Snake starting position
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            win.fill(blue)
            display_message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    x1_change, y1_change = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change, y1_change = 0, snake_block

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(white)
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
