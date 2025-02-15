import pygame
import math
import pygame.gfxdraw 

# Initialize Pygame
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)  # Default font, size 24

# Constants
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_COLOR = (255, 204, 0)
PLANET_COLORS = [(169, 169, 169),(255, 223, 186),(0, 102, 204),(255, 77, 77),(204, 153, 102),(255, 204, 102),(173, 216, 230),(0, 0, 128)]
show_orbits = True  # Initially, orbits are visible

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
pygame.display.set_caption("Solar System Simulation")

# Orbits
def draw_dashed_ellipse(surface, center, radius, color, a_scale=1.2, b_scale=0.8, dash_length=10, gap_length=5):
    for angle in range(0, 360, 15):
        start_x = center[0] + radius * math.cos(math.radians(angle)) * a_scale
        start_y = center[1] + radius * math.sin(math.radians(angle)) * b_scale
        end_x = center[0] + radius * math.cos(math.radians(angle + 10)) * a_scale
        end_y = center[1] + radius * math.sin(math.radians(angle + 10)) * b_scale
        pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), 1)

#button
def draw_button(screen):
    color = (100, 100, 100) if show_orbits else (50, 50, 50)  # Change color when off
    pygame.draw.rect(screen, color, (1130,50, 100, 30))  # Button rectangle
    text = font.render("Orbits: ON" if show_orbits else "Orbits: OFF", True, WHITE)
    screen.blit(text, (1135, 58))

def check_button_click(pos):
    global show_orbits
    button_x, button_y, button_width, button_height = 1130, 50, 100, 30  # Button position & size
    
    if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
        show_orbits = not show_orbits

#Planet Class
class Planet:
    def __init__(self, x, y, radius, color, orbit_radius, speed,ellipse_a=1.2, ellipse_b=0.8):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.orbit_radius = orbit_radius
        self.angle = 0
        # self.speed = speed  # Angular velocity
        self.speed = speed * (1.0 / math.sqrt(max(self.orbit_radius, 1)))  
        self.trail = []
        self.ellipse_a = ellipse_a  # Stretch along x-axis
        self.ellipse_b = ellipse_b  # Stretch along y-axis
    
    def draw_label(self, screen, name):
        text = font.render(name, True, WHITE)  # Create text surface
        screen.blit(text, (self.x + self.radius + 5, self.y - self.radius - 5))  # Offset label

    def update_position(self):
        self.angle += self.speed
        self.x = WIDTH // 2 + self.orbit_radius * math.cos(self.angle) * self.ellipse_a
        self.y = HEIGHT // 2 + self.orbit_radius * math.sin(self.angle) * self.ellipse_b

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
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

running = True



while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Press 'O' to toggle orbits
            if event.key == pygame.K_o:
                show_orbits = not show_orbits
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_button_click(pygame.mouse.get_pos())

    # sun.draw(screen)
    pygame.gfxdraw.filled_circle(screen, WIDTH // 2, HEIGHT // 2, 30, SUN_COLOR)
    pygame.gfxdraw.aacircle(screen, WIDTH // 2, HEIGHT // 2, 30, SUN_COLOR)
    
    
    for i, planet in enumerate(planets):
        if show_orbits:
            draw_dashed_ellipse(screen, (WIDTH // 2, HEIGHT // 2), planet.orbit_radius, WHITE)
        planet.update_position()
        planet.draw(screen)
        planet.draw_label(screen, planet_names[i])
        draw_button(screen)
    # for planet in planets:
    #     planet.update_position()
    #     planet.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
