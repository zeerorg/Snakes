import pygame
import random

pygame.init()

''' Colors '''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

'''Font'''
font = pygame.font.SysFont(None, 25)    

WIDTH = 800
HEIGHT = 600
FPS = 10
gamedisplay = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Snakes')
gamedisplay.fill(white)

def message(text, color, pos=None):
    if pos is None:
        pos = [WIDTH-8*len(text), HEIGHT/2]
    screen_text = font.render(text, True, color)
    gamedisplay.blit(screen_text,
                     [(WIDTH-(8*len(text)) - 20),
                      (HEIGHT/20)])
    pygame.display.update()

def disp_score():
    score = len(snake) - 4
    string = str(score)
    pos = [(WIDTH-(8*len(string)) - 20),
           (HEIGHT/20)]
    message(string, (0,0,0), pos)

def check_area(pos, lvl=1):
    if pos in snake[1:]:
        return False
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
food = [random.randint(10, (WIDTH/10-10))*10,
        random.randint(10, (HEIGHT/10-10))*10, 10, 10]

speed = 10
vel_x = speed
vel_y = 0

def start():
    global gameExit, snake, speed, gamedisplay, food, vel_x, vel_y
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    #print("Down")
                    prev_vel = vel_y
                    vel_y = speed if prev_vel != -speed else prev_vel
                    vel_x = 0

                elif event.key == pygame.K_UP:
                    #print("Up")
                    prev_vel = vel_y
                    vel_y = -speed if prev_vel != speed else prev_vel
                    vel_x = 0
                    
                elif event.key == pygame.K_LEFT:
                    #print("Left")
                    prev_vel = vel_x
                    vel_x = -speed if prev_vel != speed else prev_vel
                    vel_y = 0
                    
                elif event.key == pygame.K_RIGHT:
                    #print("Right")                    
                    prev_vel = vel_x
                    vel_x = speed if prev_vel != -speed else prev_vel
                    vel_y = 0

        gamedisplay.fill(white)
        for x in snake:
            pygame.draw.rect(gamedisplay, black, x, 3)

        pygame.draw.rect(gamedisplay, black, food)

        upfront = [0, 0, 0, 0]

        snake.pop(-1)
        snake.insert(0, [0, 0, 10, 10])
        snake[0][0] = snake[1][0] + vel_x
        snake[0][1] = snake[1][1] + vel_y

        tail_vel_y = snake[-2][1] - snake[-1][1]
        tail_vel_x = snake[-2][0] - snake[-2][0]

        if snake[0] == food:
            snake.append([snake[-1][0] - tail_vel_x,
                          snake[-1][1] - tail_vel_y,
                          10, 10])
            food = [random.randint(10, WIDTH/10)*10,
                    random.randint(10, HEIGHT/10)*10, 10, 10]
            while not check_area(food):
                food = [random.randint(10, WIDTH/10)*10,
                        random.randint(10, HEIGHT/10)*10, 10, 10]

        #if snake[0] in snake[1::]:
        #    gameExit = True
        
        disp_score()
        pygame.display.update()
        if not gameExit:
            gameExit = not check_area(snake[0])
        pyClock.tick(FPS)

    pygame.quit()
    quit()

start()
