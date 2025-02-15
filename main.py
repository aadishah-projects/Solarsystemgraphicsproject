import pygame
import math
import pygame.gfxdraw 

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_COLOR = (255, 204, 0)
PLANET_COLORS = [(169, 169, 169),(255, 223, 186),(0, 102, 204),(255, 77, 77),(204, 153, 102),(255, 204, 102),(173, 216, 230),(0, 0, 128)]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
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
        # self.speed = speed  # Angular velocity
        self.speed = speed * (1.0 / math.sqrt(max(self.orbit_radius, 1)))  
        self.trail = []

    def update_position(self):
        self.angle += self.speed
        self.x = WIDTH // 2 + self.orbit_radius * math.cos(self.angle)
        self.y = HEIGHT // 2 + self.orbit_radius * math.sin(self.angle)

        # Store the position for the trail 
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 150:  # Limit trail length
            self.trail.pop(0)

    def draw_trail(self, screen):
        # for point in self.trail:
        #     pygame.draw.circle(screen, self.color, point, 2)  # Small dots for trail
        # if len(self.trail) > 2:  # Ensure enough points for a smooth curve
        #     pygame.draw.aalines(screen, self.color,False, self.trail)
        for i in range(len(self.trail) - 1):
            alpha = int(255 * (i / len(self.trail)))  # Fades from 0 to 255
            faded_color = (*self.color, alpha)  # Apply transparency
            pygame.gfxdraw.line(screen, *self.trail[i], *self.trail[i + 1], faded_color)

    def draw(self, screen):
        # pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        self.draw_trail(screen)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.color)  # Smooth circle
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.color)  # Anti-aliasing

# Solar System Objects
sun = Planet(640, 360, 30, SUN_COLOR, 0, 0)
planets = [
    Planet(WIDTH // 2, HEIGHT // 2, 10, PLANET_COLORS[0], 60, 0.08),
    Planet(WIDTH // 2, HEIGHT // 2, 12, PLANET_COLORS[1], 110, 0.06),
    Planet(WIDTH // 2, HEIGHT // 2, 14, PLANET_COLORS[2], 160, 0.05),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[3], 210, 0.04),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[4], 320, 0.02),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[5], 420, 0.015),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[6], 520, 0.01),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[7], 600, 0.07)
]

clock = pygame.time.Clock()
FPS = 144
# Main loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sun.draw(screen)
    pygame.gfxdraw.filled_circle(screen, WIDTH // 2, HEIGHT // 2, 30, SUN_COLOR)
    pygame.gfxdraw.aacircle(screen, WIDTH // 2, HEIGHT // 2, 30, SUN_COLOR)

    for planet in planets:
        planet.update_position()
        planet.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
