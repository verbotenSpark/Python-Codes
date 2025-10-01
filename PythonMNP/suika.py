import pygame
import random as rnd
from pygame.math import Vector2
import keyboard
import sys


pygame.init()

#screen dimensions
WIDTH = 1000   #set screen width
HEIGHT = 800   #set screen height
screen = pygame.display.set_mode([WIDTH,HEIGHT])   #set screen display
run = True

#timer
fps = 60                      #simulation fps
timer = pygame.time.Clock()   #simulation timer

box_width = 600
box_height = 400
cell_size = 100
grid = {}    
class Box:
    def __init__(self,position,color = "black",line_width = 6):
        self.position = Vector2(position)
        self.color = color
        self.line_width = line_width

    def draw(self):
        pygame.draw.rect(screen,"gray",(self.position.x,self.position.y-400,600,400))
        pygame.draw.line(screen,self.color,(self.position.x-3,self.position.y),(self.position.x-3,self.position.y - box_height),self.line_width)  #left
        pygame.draw.line(screen,self.color,(self.position.x+3 + box_width,self.position.y),(self.position.x+box_width+3,self.position.y - box_height),self.line_width) #right
        pygame.draw.line(screen,self.color,(self.position.x,self.position.y+3),(self.position.x+box_width,self.position.y+3),self.line_width) #bottom

gravity = 0.5
wall_collide_retention = 0.2
ball_collide_retention = 2
friction = 1
bounce_stop = 0.7
class Ball:
    def __init__(self,color,radius,position,level = 1,velocity = (0,0),mass = 1):
        self.color = color
        self.radius = radius
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.terminal_velocity = 5
        self.mass = mass
        self.level = level

    def draw(self):
        pygame.draw.circle(screen,self.color,self.position,self.radius)
        startx = self.position.x
        starty = self.position.y
        pygame.draw.line(screen,"white",(startx,starty),(startx+5*self.velocity.x,starty+ 5*self.velocity.y),5)

    # def update_gravity(self):
        

    def update(self):

        ball_bottom = self.position.y + self.radius  #base of ball

        if ball_bottom < box.position.y:             #if base of ball is above base of box 
            if self.velocity.y < self.terminal_velocity:
                self.velocity.y += gravity         #move towards base

        elif ball_bottom>=box.position.y:            #if base of ball is at base or below base of box

            self.velocity.y = 0                  #else stop
            if self.position.y > box.position.y-self.radius:
                self.position.y = box.position.y - self.radius


        if (self.position.x < box.position.x + self.radius and self.velocity.x < 0) or                                                                      (self.position.x > box.position.x + box_width - self.radius and self.velocity.x > 0):  
            #if ball is touching the left wall and velocity is -ve  or touching the right wall and velocity is +ve 
            self.velocity.x *= -1*wall_collide_retention    #reverse velocity direction
            if(abs(self.velocity.x) < bounce_stop):         #if velocity is very less
                    self.velocity.x = 0                     #stop
        elif (self.position.x > box.position.x and self.position.x < box.position.x + box_width) and self.velocity.x > 0:
            self.velocity.x *= 0.7

        if self.position.x < box.position.x + self.radius:
            self.position.x = box.position.x + self.radius
        elif self.position.x > box.position.x + box_width - self.radius:
            self.position.x = box.position.x + box_width - self.radius
            
        if abs(self.velocity.y) < 0.1 and abs(self.velocity.x) < 0.5:
            touching = 0
            for other in ball_list:
                if other is not self:
                    dist = (self.position - other.position).length()
                    if dist < self.radius + other.radius + 5:
                        touching += 1
            if touching >= 2:
                self.velocity.x = 0  # stop sliding
        # if abs(self.velocity.y) < 0.1:
        #     self.velocity.y = 0

        if self.position.x < box.position.x - box_height + self.radius:
            run = False
        self.position += self.velocity

    def combine_balls(self,other,level):
        new_posx = (self.position.x + other.position.x)/2
        new_posy = (self.position.y + other.position.y)/2

        new_pos = Vector2(new_posx,new_posy)
        #make new ball of higher level add to a ball list 

    def check_collision(self,other):
        impactVct = other.position - self.position
        d = impactVct.length()
        if (d < self.radius + other.radius):
            if (self.radius == other.radius):
                newxpos = (self.position.x + other.position.x)/2
                newypos = (self.position.y + other.position.y)/2

                self.radius+= 10
                self.position = Vector2(newxpos,newypos)
                radius_diff = self.radius - 10
                self.position.y -= radius_diff  # lift the ball up to prevent overlap
                return other
            else:
                overlap = d - (other.radius + self.radius)
                dir = impactVct.normalize() * (overlap/2)
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
                # self.velocity.x *= 0.3
                # self.velocity.y *= 0.3

                delVB = impactVct * (-2*self.mass * num/den)
                other.velocity += delVB
                # other.velocity.x = 0
                # other.velocity *= 0.8

ball_list = []
class Balls:
    def __init__(self):
        pass
        self.ball1 = Ball("red",30,(350,50),3,(1,0))
        self.ball2 = Ball("green",50,(450,50),5,(-4,0))
        # ball_list.append(Ball('yellow',1,(-10,0),(0,0),1))
        ball_list.append(self.ball1)
        ball_list.append(self.ball2)


    def draw(self):
        for ball in ball_list:
            ball.draw()

    def update(self):
        # for ball in ball_list:
        to_remove = []
        for i in range(len(ball_list)):
            ball_list[i].update()
            pa = ball_list[i]
            for j in range(i+1,len(ball_list)):
                pb = ball_list[j]
                result = pa.check_collision(pb)
                if result is not None:
                    to_remove.append(result)
        for ball in to_remove:
            if ball in ball_list:
                ball_list.remove(ball)

class UI:
    def __init__(self,posx = 500):
        self.posx = posx
        self.posy = 150
        self.tapped = False
    


    def update(self):
        
        if keyboard.is_pressed("a") and self.posx > 220:
            self.posx -= 4
        elif keyboard.is_pressed("d") and self.posx < 780:
            self.posx += 4
        if self.tapped == True:
            radius = rnd.randint(40,45)
            bal = Ball(rnd.randint(55,200),radius,ui.position(),radius-40)
            ball_list.append(bal)
            pygame.draw.circle(screen,bal.color,(self.posx,150),bal.radius)
        self.tapped = False
            
    def draw(self):
        pygame.draw.line(screen,"brown",(self.posx-1,self.posy),(self.posx-1,self.posy+300),2)
        # pygame.draw.circle(screen,"pink",(self.posx,150),10)

    def position(self):
        return self.posx,self.posy








box = Box((200,700))
ball0 = Balls()
ui = UI()
ball_types = [Ball('red',10,ui.position()),Ball('yellow',20,ui.position())]
while run:                    #while run is true keep updating and repainting the screen
    timer.tick(fps)           #tick timer based on fps
    screen.fill((155,155,0))      #fill screen with said color
    box.draw()
    ball0.draw()
    ball0.update()
    ui.draw()
    ui.update()
    for event in pygame.event.get():   #event handler/ input handler
        if event.type == pygame.QUIT:  #if red cross is pressed 
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                ui.tapped = True

    pygame.display.flip()    #redraw the screen
pygame.quit()