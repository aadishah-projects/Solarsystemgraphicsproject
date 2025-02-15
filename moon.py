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
    
    def update_position(self,zoom_factor, pan_x, pan_y):
        self.angle += self.speed

        # Debug by Deepseek: 
        self.x = self.planet.x + self.orbit_radius * zoom_factor * math.cos(self.angle)
        self.y = self.planet.y + self.orbit_radius * zoom_factor * math.sin(self.angle)
        
    def draw_orbit(self, screen, zoom_factor, pan_x, pan_y):
        #  """Draw moon orbit with zoom and panning."""
        # zoomed_x = (self.planet.x - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
        # zoomed_y = (self.planet.y - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
        # zoomed_radius = self.orbit_radius * zoom_factor
        pygame.draw.circle(
        screen, 
        (100, 100, 100), 
        (int(self.planet.x), int(self.planet.y)), 
        int(self.orbit_radius * zoom_factor), 
        1
    )
    def draw(self, screen, zoom_factor, pan_x, pan_y):
        # """Draw the moon at its updated position."""
        # Moon's position is already correct; only scale its size
        zoomed_size = max(1, int(self.size * zoom_factor))
        pygame.draw.circle(
            screen, 
            self.color, 
            (int(self.x), int(self.y)), 
            zoomed_size
        )