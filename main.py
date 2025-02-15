import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_COLOR = (255, 204, 0)
PLANET_COLORS = [(169, 169, 169),(255, 223, 186),(0, 102, 204),(255, 77, 77),(204, 153, 102),(255, 204, 102),(173, 216, 230),(0, 0, 128)]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Planet Class
class Planet:
    def __init__(self, x, y, radius, color, orbit_radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.orbit_radius = orbit_radius
        self.angle = 0
        self.speed = speed  # Angular velocity

    def update_position(self):
        self.angle += self.speed
        self.x = WIDTH // 2 + self.orbit_radius * math.cos(self.angle)
        self.y = HEIGHT // 2 + self.orbit_radius * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Solar System Objects
sun = Planet(640, 360, 30, SUN_COLOR, 0, 0)
planets = [
    Planet(WIDTH // 2, HEIGHT // 2, 10, PLANET_COLORS[0], 60, 0.003),
    Planet(WIDTH // 2, HEIGHT // 2, 12, PLANET_COLORS[1], 110, 0.0025),
    Planet(WIDTH // 2, HEIGHT // 2, 14, PLANET_COLORS[2], 160, 0.002),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[3], 210, 0.0017),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[4], 320, 0.0009),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[5], 420, 0.0007),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[6], 520, 0.0005),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[7], 600, 0.0004)
]

# Main loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sun.draw(screen)

    for planet in planets:
        planet.update_position()
        planet.draw(screen)

    pygame.display.update()

pygame.quit()
