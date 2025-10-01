import pygame 
import random as rnd
from pygame.math import Vector2
import keyboard
import time

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH,HEIGHT])
grid_side_len = 30
maxScore = 599
run = True

class cube:
    def __init__(self,sideLen = grid_side_len,color = 'white'):
        self.side = sideLen
        self.color = color
        self.position = Vector2(300,300)
        self.score = 0
        self.direction = 'up'
        self.speedBoost = False
        self.lastPos = Vector2(0,0)
        self.completed = False
    

    def update(self):
        self.lastPos = self.position/grid_side_len
        if(self.speedBoost == True):
            distance = grid_side_len*1.5
        else:
            distance = grid_side_len
        if self.direction == 'up':
            self.position.y -= distance
        elif self.direction == 'down':
            self.position.y += distance
        elif self.direction == 'left':
            self.position.x -= distance
        elif self.direction == 'right':
            self.position.x += distance


        if self.position.y < 0:
            self.position.y = HEIGHT-grid_side_len
        elif self.position.y > HEIGHT-grid_side_len:
            self.position.y = 0
        elif self.position.x < 0:
            self.position.x = WIDTH-grid_side_len
        elif self.position.x > WIDTH-grid_side_len:
            self.position.x = 0

        if head.position in tail_list.positions:
            self.score = 0
            tail_list.reset()

    def checkKey(self):
        if keyboard.is_pressed('w') and self.direction != 'down':
            self.direction = 'up'
        elif keyboard.is_pressed('s') and self.direction != 'up':
            self.direction = 'down'
        elif keyboard.is_pressed('a') and self.direction != 'right':
            self.direction = 'left'
        elif keyboard.is_pressed('d') and self.direction != 'left':
            self.direction = 'right'
        elif keyboard.is_pressed('e'):
            self.speedBoost = True
        elif keyboard.is_pressed('e') == False:
            self.speedBoost = False

    def draw(self):
        pygame.draw.rect(screen,self.color,(self.position.x,self.position.y,self.side,self.side))

class food:
    def __init__(self,color = 'red'):
        self.position = Vector2(grid_side_len*rnd.randint(2,10),grid_side_len*rnd.randint(2,10))
        self.alive = True
        self.color = color

    def draw(self):
        side = grid_side_len
        pygame.draw.circle(screen,self.color,self.position+Vector2(15,15),side/2)

    def update(self):
        if head.position == self.position:
            head.score+=1
            temp_color = self.color
            self.color = (rnd.randint(55,255),rnd.randint(55,255),rnd.randint(55,255))
            tail_list.add_segment(temp_color)
            self.position = Vector2(grid_side_len*rnd.randint(2,20),grid_side_len*rnd.randint(2,15))

class score_data:
    pygame.font.init()
    def __init__(self,str=None,color = 'yellow'):
        self.str = str
        self.scor = head.score
        self.color = color
    def draw(self):
        font = pygame.font.SysFont('arial',48)
        text_surface = font.render(str(self.scor),False,(0,255,255))
        screen.blit(text_surface,(10,10))
    def update(self):
        self.scor = head.score
        if tail_list.length >= maxScore:
            drawWin()
def drawWin():
    font = pygame.font.SysFont('arial',56)
    text_surface = font.render("Game Completed",False,(0,255,255))
    screen.blit(text_surface,(200,200))
    head.completed = True

class tail:
    def __init__(self, color='gray'):
        self.color = color
        self.positions = []  # Stores past head positions
        self.colors = []
        self.side = grid_side_len
        self.length = 0  # Number of tail segments

    def add_segment(self,color):
        self.length += 1
        self.colors.insert(0,color)

    def update(self, head_pos):
        self.positions.insert(0, Vector2(head_pos))  # Insert current head position
        if len(self.positions) > self.length:
            self.positions.pop()  # Remove oldest position if exceeding length
        if len(self.colors) > self.length:
            self.colors.pop()

    def draw(self):
        for i in range(len(self.positions)):
            pygame.draw.circle(screen, self.colors[i], self.positions[i] + Vector2(15, 15), self.side / 2)

    def reset(self):
        self.positions = []
        self.length = 0

fps = 30
timer = pygame.time.Clock()

head = cube(30)
tail_list = tail()
apple = food()
cur_score = score_data()
tail_list = tail()
screen_fps = 0
while run:
    timer.tick(fps)
    if head.completed == False:
        head.checkKey()
        cur_score.update()
    else:
        time.sleep(2)
        run = False
    screen_fps = (screen_fps + 1)%8  #screen_fps is 1/10th of actual fps
    if screen_fps == 0:
        screen.fill('black')
        apple.update()
        apple.draw()
        tail_list.update(head.position)  # Update with current head position
        tail_list.draw()

        head.update()
        head.draw()
        cur_score.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()