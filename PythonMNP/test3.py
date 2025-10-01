import pygame
import random
import math

WIDTH, HEIGHT = 640, 360

class Particle:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.velocity = pygame.Vector2(math.cos(angle) * speed, math.sin(angle) * speed)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = random.uniform(2, 6)
        self.r = math.sqrt(self.mass) * 20
    
    def apply_force(self, force):
        f = force / self.mass
        self.acceleration += f
    
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0
    
    def collide(self, other):
        impact_vector = other.position - self.position
        d = impact_vector.length()
        if d < self.r + other.r:
            overlap = d - (self.r + other.r)
            dir_vector = impact_vector.normalize() * (overlap * 0.5)
            self.position += dir_vector
            other.position -= dir_vector
            
            d = self.r + other.r
            impact_vector = impact_vector.normalize() * d
            
            m_sum = self.mass + other.mass
            v_diff = other.velocity - self.velocity
            num = v_diff.dot(impact_vector)
            den = m_sum * d * d
            
            delta_va = impact_vector * (2 * other.mass * num / den)
            delta_vb = impact_vector * (-2 * self.mass * num / den)
            
            self.velocity += delta_va
            other.velocity += delta_vb
    
    def edges(self):
        if self.position.x > WIDTH - self.r:
            self.position.x = WIDTH - self.r
            self.velocity.x *= -1
        elif self.position.x < self.r:
            self.position.x = self.r
            self.velocity.x *= -1
        
        if self.position.y > HEIGHT - self.r:
            self.position.y = HEIGHT - self.r
            self.velocity.y *= -1
        elif self.position.y < self.r:
            self.position.y = self.r
            self.velocity.y *= -1
    
    def show(self, screen):
        pygame.draw.circle(screen, (127, 127, 127), (int(self.position.x), int(self.position.y)), int(self.r))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

particleA = Particle(320, 60)
particleB = Particle(320, 300)

running = True
while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    particleA.collide(particleB)
    particleA.update()
    particleB.update()
    particleA.edges()
    particleB.edges()
    particleA.show(screen)
    particleB.show(screen)
    
    speedA = particleA.velocity.length()
    speedB = particleB.velocity.length()
    kinA = 0.5 * particleA.mass * speedA ** 2
    kinB = 0.5 * particleB.mass * speedB ** 2
    print(kinA + kinB)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
