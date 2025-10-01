import pygame
import random
import math

WIDTH, HEIGHT = 1000, 800

global_gravity = 0
global_friction = 0
global_retention = 1

class Particle:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.velocity = pygame.Vector2(math.cos(angle) * speed, math.sin(angle) * speed)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = random.uniform(2, 6)
        self.r = math.sqrt(self.mass) * 20
        self.color = (127, 127, 127)
    
    def apply_force(self, force):
        f = force / self.mass
        self.acceleration += f
    
    def update(self):
        self.velocity *= (1 - global_friction)
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
            
            delta_va = impact_vector * (2 * other.mass * num / den) * global_retention
            delta_vb = impact_vector * (-2 * self.mass * num / den) * global_retention
            
            self.velocity += delta_va
            other.velocity += delta_vb
    
    def edges(self):
        if self.position.x > WIDTH - self.r:
            self.position.x = WIDTH - self.r
            self.velocity.x *= -global_retention
        elif self.position.x < self.r:
            self.position.x = self.r
            self.velocity.x *= -global_retention
        
        if self.position.y > HEIGHT - self.r:
            self.position.y = HEIGHT - self.r
            self.velocity.y *= -global_retention
        elif self.position.y < self.r:
            self.position.y = self.r
            self.velocity.y *= -global_retention
    
    def show(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), int(self.r))

def draw_slider(screen, x, y, value, label):
    pygame.draw.rect(screen, (200, 200, 200), (x, y, 300, 5))
    pygame.draw.circle(screen, (0, 0, 0), (x + int(value * 300), y + 2), 7)
    font = pygame.font.Font(None, 24)
    text = font.render(f"{label}: {value:.2f}", True, (0, 0, 0))
    screen.blit(text, (x + 320, y - 5))

def highlight_fastest(particles):
    fastest = max(particles, key=lambda p: p.velocity.length())
    for p in particles:
        p.color = (127, 127, 127)
    fastest.color = (255, 0, 0)

def shoot_particle(mx, my):
    start_x, start_y = WIDTH // 2, HEIGHT // 2
    direction = pygame.Vector2(mx - start_x, my - start_y)
    if direction.length() > 0:
        direction = direction.normalize() * min(direction.length() * 0.1, 10)
    new_particle = Particle(start_x, start_y)
    new_particle.velocity = direction
    particles.append(new_particle)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

particles = [Particle(400, 60), Particle(400, 300)]

running = True
while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            shoot_particle(mx, my)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            if 100 <= mx <= 400:
                if HEIGHT - 120 <= my <= HEIGHT - 110:
                    global_gravity = (mx - 100) / 300
                elif HEIGHT - 90 <= my <= HEIGHT - 80:
                    global_friction = (mx - 100) / 300
                elif HEIGHT - 60 <= my <= HEIGHT - 50:
                    global_retention = (mx - 100) / 300
    
    gravity_force = pygame.Vector2(0, global_gravity)
    for p in particles:
        p.apply_force(gravity_force)
    
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            particles[i].collide(particles[j])
    
    for p in particles:
        p.update()
        p.edges()
    
    highlight_fastest(particles)
    
    for p in particles:
        p.show(screen)
    
    draw_slider(screen, 100, HEIGHT - 120, global_gravity, "Gravity")
    draw_slider(screen, 100, HEIGHT - 90, global_friction, "Friction")
    draw_slider(screen, 100, HEIGHT - 60, global_retention, "Retention")
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
