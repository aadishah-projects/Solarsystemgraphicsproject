from import_init import*
from settings import*

#Planet Class
class Planet:
    def __init__(self,name, x, y, radius, color, texture_path, orbit_radius, speed,rotation_speed,ellipse_a=1.2, ellipse_b=0.8):
        self.name = name
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

    def update_position(self,zoom_factor, pan_x, pan_y,global_speed_factor):
        # Orbital motion
        self.angle += self.speed * global_speed_factor
        self.x = WIDTH // 2 + self.orbit_radius * math.cos(self.angle) * self.ellipse_a *zoom_factor + pan_x
        self.y = HEIGHT // 2 + self.orbit_radius * math.sin(self.angle) * self.ellipse_b * zoom_factor + pan_y

        # Store the position for the trail 
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 150:  # Limit trail length
            self.trail.pop(0)
        
        #Rotational motion
        self.rotation_angle += self.rotation_speed
   

    def draw_trail(self, screen,zoom_factor, pan_x, pan_y):
        if len(self.trail) < 2:
            return  # Not enough points to draw a smooth curve

        # transformed_trail = []
        # for x, y in self.trail:
        # # Keep trails attached to planet and apply zoom/pan correctly
        #     zoomed_x = ((x - WIDTH // 2) * zoom_factor) + WIDTH // 2 + pan_x
        #     zoomed_y = ((y - HEIGHT // 2) * zoom_factor) + HEIGHT // 2 + pan_y
        #     transformed_trail.append((int(zoomed_x), int(zoomed_y)))

        # Smooth trail rendering
        pygame.draw.aalines(screen, self.color, False, self.trail)
    
    def draw(self, screen,zoom_factor, pan_x, pan_y):
        # pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        scaled_radius = int(self.radius * zoom_factor)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), scaled_radius, self.color)  # Smooth circle
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), scaled_radius, self.color) 

    def draw_textures(self,screen,zoom_factor, pan_x , pan_y):
        # Apply zoom to texture size
        scaled_size = int(self.radius * 2 * zoom_factor)
        scaled_texture = pygame.transform.scale(self.image, (scaled_size, scaled_size))

        rotated_texture = pygame.transform.rotate(scaled_texture, -self.rotation_angle)


        # Apply zoom & pan to position
        draw_x = (self.x - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
        draw_y = (self.y - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y


        rect = rotated_texture.get_rect(center=(int(self.x), int(self.y)))
        # screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        screen.blit(rotated_texture, rect.topleft)
