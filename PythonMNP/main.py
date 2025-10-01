import pygame
import random as rnd
from pygame.math import Vector2

pygame.init()  #initialize all modules of pygame

#screen dimensions
WIDTH = 1000   #set screen width
HEIGHT = 800   #set screen height
screen = pygame.display.set_mode([WIDTH,HEIGHT])   #set screen display

#timer
fps = 60                      #simulation fps
timer = pygame.time.Clock()   #simulation timer

#game variables
gravity = 0       #gravity of the simulation
bounce_stop = 0.1   #the y speed below which the ball will not bounce
mouse_vector_list = []  #will store position of the mouse
space = False

# game classes
class Ball:            #ball class
    def __init__(self,x_pos,y_pos,radius,color,mass,friction,retention):  #define attributes of ball
        #similar to a constructor ^^
        self.position = Vector2(x_pos,y_pos)
        self.radius = radius
        self.color = color
        self.mass = mass
        self.friction = friction
        self.retention = retention
        self.velocity = Vector2(0,0)
        self.circle = ""
        self.selected = False
        self.defcolor = color
    
    def draw(self):    #method to draw the ball
        self.circle = pygame.draw.circle(screen,self.color,self.position,self.radius)
        startx = self.position.x
        starty = self.position.y
        pygame.draw.line(screen,"white",(startx,starty),(startx+5*self.velocity.x,starty+ 5*self.velocity.y),5)

    def check_gravity(self):
        if not self.selected:
            if space == True:
                gravity = 0
                self.retention = 1
                self.friction = 0
                bounce_stop = 0
            else:
                gravity = 0.5
                self.retention   = 0.6
                # self.friction    = 0.1
                bounce_stop = 0.1

            if self.position.y < HEIGHT - self.radius:   #^check if ball is above the screen
                if space == False:
                    self.velocity.y += gravity       #<then move towards the ground
            else:
                if self.velocity.y > bounce_stop:           #if ball y speed is more than bounce stop speed
                    self.velocity.y *= -1 * self.retention  #flip the ball speed,retention slow down
                else:
                    self.velocity.y = 0
                    
            if self.position.y < self.radius:
                self.position.y = self.radius
                self.velocity.y *= -1 * self.retention
            elif self.position.y > HEIGHT-self.radius:
                self.position.y = HEIGHT - self.radius
                # self.velocity.y = 0
            

                
            if((self.position.x < self.radius and self.velocity.x < 0) or
                (self.position.x > WIDTH - self.radius and self.velocity.x > 0)):
                self.velocity.x *= -1 *self.retention

                if(abs(self.velocity.x) < bounce_stop):
                    self.velocity.x = 0
            if self.position.x - self.radius < 0:
                self.position.x = self.radius
            elif self.position.x + self.radius > WIDTH:
                self.position.x = WIDTH - self.radius
            if self.position.y+self.radius == HEIGHT and self.velocity.x != 0 and self.velocity.x > bounce_stop:
                self.retention = 0.98
            else:
                self.retention = 0.6
            #     if self.velocity.x > 0:
            #         self.velocity.x -= self.friction
            #     elif self.velocity.x < 0:
            #         self.velocity.x += self.friction
        else:
            self.velocity.x = x_push
            self.velocity.y = y_push
        # return self.velocity.y

    def update_pos(self, point):
        if not self.selected:
            self.position += self.velocity
        elif self.selected:
            self.position.x = point[0]
            self.position.y = point[1]

    def check_select(self,pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected

    def check_collision(self,other):
        impactVct = other.position - self.position
        d = impactVct.length()
        if (d < self.radius + other.radius):
            
            self.color = 'red'
            overlap = d - (other.radius + self.radius)
            dir = impactVct.normalize() * (overlap * 0.5)
            print(impactVct,impactVct.normalize())
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
            self.velocity *= 0.9

            delVB = impactVct * (-2*self.mass * num/den)
            other.velocity += delVB
            # other.velocity *= 0.8
            get_kin_energy(ball_list)
        else:
            # self.velocity = 0
            self.color = self.defcolor

def get_kin_energy(ball_list):
    spd_list = []
    kin_list = []
    kin = 0
    for i in range(len(ball_list)):
        spd_list.append(ball_list[i].velocity.length())
        kin_list.append(0.5 * ball_list[i].mass * spd_list[i] ** 2)
        kin += kin_list[i]
    # if kin < 1.4:
    #     for ball in ball_list:
    #         ball.velocity = Vector2(0,0)
    print(kin)
    spd_list.clear()
    kin_list.clear()

#game methods

def calc_mouse_vector():
    x_speed = 0
    y_speed = 0
    if(len(mouse_vector_list) > 10):
        x_speed = (mouse_vector_list[-1][0] - mouse_vector_list[0][0])/len(mouse_vector_list)
        y_speed = (mouse_vector_list[-1][1] - mouse_vector_list[0][1])/len(mouse_vector_list)
    return x_speed,y_speed



#game objects
# ball1 = Ball(50,50,30,'yellow',1,0.02,.7)        #define ball1 with its attributes
# ball2 = Ball(300,300,50,'pink',3,0.03,.8)        #define ball2 with its attributes
# ball_list = [ball1,ball2]

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
for i in range(30):
    x = rnd.randint(50,800)
    y = rnd.randint(50,800)
    ball_list.append(Ball(x,y,rnd.randint(50,70),'grey',rnd.randint(10,20),.02,.85))

#game loop
run = True
while run:                    #while run is true keep updating and repainting the screen
    timer.tick(fps)           #tick timer based on fps
    screen.fill('black')      #fill screen with said color
    mouse_coords = pygame.mouse.get_pos()
    mouse_vector_list.append(mouse_coords)
    if(len(mouse_vector_list) > 20):
        mouse_vector_list.pop(0)
    x_push,y_push = calc_mouse_vector()

    fastestBall(ball_list)
    for ball in ball_list:
        ball.draw()
        ball.check_gravity()
        ball.update_pos(mouse_coords)
    
    # ball2.check_collision(ball1)
    for i in range(len(ball_list)):
        pa = ball_list[i]
        for j in range(i+1,len(ball_list)):
            pb = ball_list[j]
            pa.check_collision(pb)

    for event in pygame.event.get():   #event handler/ input handler
        if event.type == pygame.QUIT:  #if red cross is pressed 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for ball in ball_list:
                    if(ball.check_select(event.pos)):
                        active_select = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_select = False
                for ball in ball_list:
                    ball.check_select((-1000,-1000))

        
    pygame.display.flip()    #redraw the screen
pygame.quit()