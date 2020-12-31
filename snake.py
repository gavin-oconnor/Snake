import pygame
import random

win = pygame.display.set_mode((500,500))
run = True
clock = pygame.time.Clock()
snake = [(100,250)]
food  = (300,400)
direction = 0
last = None
et = 0

def drawGrid():
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(win,(255,255,255),(y*50,x*50,50,50),1)

def checkHead(xy):
    global snake, direction
    if xy in snake:
        snake = [(100,250)]
        direction = 0
        return True
    elif xy[0] < 0 or xy[0] > 500:
        snake = [(100,250)]
        direction = 0
        return True
    elif xy[1] < 0 or xy[1] > 500:
        snake = [(100,250)]
        direction = 0
        return True

def right():
    global last
    if checkHead((snake[0][0]+50,snake[0][1])):
        return
    snake.insert(0,(snake[0][0]+50,snake[0][1]))
    last = snake.pop()

def left():
    global last
    if checkHead((snake[0][0]-50,snake[0][1])):
        return
    snake.insert(0,(snake[0][0]-50,snake[0][1]))
    last = snake.pop()

def up():
    global last
    if checkHead((snake[0][0],snake[0][1]-50)):
        return
    snake.insert(0,(snake[0][0],snake[0][1]-50))
    last = snake.pop()

def down():
    global last
    if checkHead((snake[0][0],snake[0][1]+50)):
        return
    snake.insert(0,(snake[0][0],snake[0][1]+50))
    last = snake.pop()

def checkFood():
    global food
    if snake[0] == food:
        if last:
            snake.append(last)
        food = (random.randint(0,9)*50,random.randint(0,9)*50)

def drawFood():
    pygame.draw.rect(win,(0,255,0),(food[0]+2,food[1]+2,46,46))



def drawSnake():
    for ele in snake:
        pygame.draw.rect(win,(255,255,255),(ele[0]+2,ele[1]+2,46,46))
        
functions = [right,up,left,down]

i = 0
while run:
    '''if i < 30:
        i += 1
    else:
        i = 0'''
    dt = clock.tick(30)
    et += dt
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and direction != 3:
                    direction = 1
                if event.key == pygame.K_DOWN and direction != 1:
                    direction = 3
                if event.key == pygame.K_RIGHT and direction != 2:
                    direction = 0
                if event.key == pygame.K_LEFT and direction != 0:
                    direction = 2
    '''KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_SPACE]:
        if direction <= 2:
            direction += 1
        else:
            direction = 0'''
    #if i%6 == 0:
    if et > 250:
        functions[direction]()
        et = 0
    win.fill((0,0,0))
    drawGrid()
    drawFood()
    drawSnake()
    checkFood()
    pygame.display.update()