import random as rnd; import math; import pygame
from pygame.math import Vector2

pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 60

class particle:
    def __init__(self,x,y):
        self.position = Vector2(x,y)
        self.velocity = Vector2(rnd.randint(3,7),rnd.randint(3,7))
        # self.velocity = Vector2(5,5)
        self.mass = rnd.randint(5,15)
        self.radius = math.sqrt(self.mass)*10
        self.color = 'grey'

    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
    
    def edges(self):
        if(self.position.x > WIDTH - self.radius):
            self.position.x = WIDTH - self.radius
            self.velocity.x *= -1
        elif(self.position.x < self.radius):
            self.position.x = self.radius
            self.velocity.x *= -1

        if(self.position.y > HEIGHT - self.radius):
            self.position.y = HEIGHT - self.radius
            self.velocity.y *= -1
        elif(self.position.y < self.radius):
            self.position.y = self.radius
            self.velocity.y *= -1
    
    def draw(self):
        self.circle = pygame.draw.circle(screen,self.color,self.position,self.radius)
    
    def collide(self,other):
        impactVct = other.position - self.position
        d = impactVct.length()
        if (d < self.radius + other.radius):
            overlap = d - (other.radius + self.radius)
            dir = impactVct.normalize() * (overlap * 0.5)
            self.position += dir
            other.position -= dir

            d = other.radius + self.radius
            impactVct = impactVct.normalize() * d

            masSum = self.mass + other.mass
            vDiff = other.velocity - self.velocity

            num = vDiff.dot(impactVct)
            den = masSum *d *d

            delVA = impactVct * (2*other.mass*num/den)
            self.velocity += delVA

            delVB = impactVct * (-2*self.mass * num/den)
            other.velocity += delVB

def get_vel_len(ball):
    return ball.velocity.length()

def fastestBall(ball_list):
    fastest = max(ball_list,key = get_vel_len)
    slowest = min(ball_list,key = get_vel_len)
    for p in ball_list:
        p.color = 'grey'
    slowest.color = 'green'
    fastest.color = 'red'


ball_list= []
for i in range(20):
    x = rnd.randint(1,800)
    y = rnd.randint(1,800)
    ball_list.append(particle(x,y))

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    fastestBall(ball_list)
    for ball in ball_list:
        ball.update()
        ball.draw()
        ball.edges()
    
    #ball1.collide(ball2)
    for i in range(len(ball_list)):
        pa = ball_list[i]
        for j in range(i+1,len(ball_list)):
            pb = ball_list[j]
            pa.collide(pb)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()