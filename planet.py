from import_init import*
from settings import*

#Planet Class
class Planet:
    def __init__(self, x, y, radius, color, texture_path, orbit_radius, speed,rotation_speed,ellipse_a=1.2, ellipse_b=0.8):
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
        
         # Load texture
        self.image = pygame.image.load(texture_path)
        self.image = pygame.transform.scale(self.image, (2 * radius, 2 * radius))
        
        # Rotation
        self.rotation_angle = 0  # Start at 0 degrees
        self.rotation_speed = rotation_speed  # Speed of self-rotation

    def draw_label(self, screen, name):
        text = font.render(name, True, WHITE)  # Create text surface
        screen.blit(text, (self.x + self.radius + 5, self.y - self.radius - 5))  # Offset label

    def update_position(self):
        # Orbital motion
        self.angle += self.speed
        self.x = WIDTH // 2 + self.orbit_radius * math.cos(self.angle) * self.ellipse_a
        self.y = HEIGHT // 2 + self.orbit_radius * math.sin(self.angle) * self.ellipse_b

        # Store the position for the trail 
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 150:  # Limit trail length
            self.trail.pop(0)
        
        #Rotational motion
        self.rotation_angle += self.rotation_speed
   

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
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.color) 

    def draw_textures(self,screen):
        self.draw_trail(screen)

        rotated_texture = pygame.transform.rotate(self.image, -self.rotation_angle)
        rect = rotated_texture.get_rect(center=(int(self.x), int(self.y)))

        # screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        screen.blit(rotated_texture, rect.topleft)
