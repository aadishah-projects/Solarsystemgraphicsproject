from import_init import*
from settings import*

class Moon:
    def __init__(self, planet, orbit_radius, size, color, speed):
        self.planet = planet  # Parent planet
        self.orbit_radius = orbit_radius
        self.size = size
        self.color = color
        self.angle = 0
        self.speed = speed  # Moon's orbit speed
    
    def update_position(self):
        self.angle += self.speed
        self.x = self.planet.x + self.orbit_radius * math.cos(self.angle)
        self.y = self.planet.y + self.orbit_radius * math.sin(self.angle)

    def draw_orbit(self, screen, zoom_factor, pan_x, pan_y):
        #  """Draw moon orbit with zoom and panning."""
        zoomed_x = (self.planet.x - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
        zoomed_y = (self.planet.y - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
        zoomed_radius = self.orbit_radius * zoom_factor
        pygame.draw.circle(screen, (100, 100, 100), (int(zoomed_x), int(zoomed_y)), int(zoomed_radius), 1)
    
    def draw(self, screen, zoom_factor, pan_x, pan_y):
        # """Draw the moon at its updated position."""
        zoomed_x = (self.x - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
        zoomed_y = (self.y - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
        zoomed_size = max(1, int(self.size * zoom_factor))  # Prevent disappearing at small zoom
        
        pygame.draw.circle(screen, self.color, (int(zoomed_x), int(zoomed_y)), zoomed_size)