import pygame
import random

pygame.init()

''' Colors '''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

WIDTH = 800
HEIGHT = 600
FPS = 10
gamedisplay = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Snakes')
gamedisplay.fill(white)

def check_area(pos, lvl=1):
    if lvl == 1:
        if pos[0] < 0 or pos[0] > WIDTH-10 or pos[1] < 0 or pos[1] > HEIGHT-10:
            return False
        else:
            return True

snake = [ [WIDTH/2+20, HEIGHT/2, 10, 10],
          [WIDTH/2+10, HEIGHT/2, 10, 10],
          [WIDTH/2,    HEIGHT/2, 10, 10],
          [WIDTH/2-10, HEIGHT/2, 10, 10] ]

pyClock = pygame.time.Clock()
gameExit = False
food = [random.randint(10, (WIDTH/10-10))*10, random.randint(10, (HEIGHT/10-10))*10, 10, 10]

speed = 10
vel_x = speed
vel_y = 0

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                prev_vel = vel_y
                vel_y = speed
                vel_x = 0
                if(prev_vel == -speed):
                    fakesnake = snake[::-1]
                    snake = fakesnake
                    
            elif event.key == pygame.K_UP:
                prev_vel = vel_y
                vel_y = -speed
                vel_x = 0
                if(prev_vel == speed):
                    fakesnake = snake[::-1]
                    snake = fakesnake

            elif event.key == pygame.K_LEFT:
                prev_vel = vel_x
                vel_x = -speed
                vel_y = 0
                if(prev_vel == speed):
                    fakesnake = snake[::-1]
                    snake = fakesnake

            elif event.key == pygame.K_RIGHT:
                prev_vel = vel_x
                vel_x = speed
                vel_y = 0
                if(prev_vel == -speed):
                    fakesnake = snake[::-1]
                    snake = fakesnake

    gamedisplay.fill(white)
    for x in snake:
        pygame.draw.rect(gamedisplay, black, x, 3)

    pygame.draw.rect(gamedisplay, black, food)

    upfront = [0, 0, 0, 0]

    snake.pop(-1)
    snake.insert(0, [0, 0, 10, 10])
    snake[0][0] = snake[1][0] + vel_x
    snake[0][1] = snake[1][1] + vel_y

    if snake[0] in snake[1::]:
        gameExit = True

    if snake[-1] == food:
        snake.append([food[0]-(snake[-2][0]-snake[-1][0]),
                      food[1]-(snake[-2][1]-snake[-1][1]),
                      10, 10])
        food = [random.randint(10, WIDTH/10)*10, random.randint(10, HEIGHT/10)*10, 10, 10]

    pygame.display.update()
    pyClock.tick(FPS)
    gameExit = not check_area(snake[0])

pygame.quit()
quit()
