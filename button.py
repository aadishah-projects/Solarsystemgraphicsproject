from import_init import*
from settings import*
#button
def draw_button_1(screen):
    color = (100, 100, 100) if show_orbits else (50, 50, 50)  # Change color when off
    pygame.draw.rect(screen, color, (1130,50, 100, 30))  # Button rectangle
    text = font.render("Orbits: ON" if show_orbits else "Orbits: OFF", True, WHITE)
    screen.blit(text, (1135, 58))

def draw_button_2(screen):
    color = (150, 150, 150) if show_textures else (50, 50, 50)  # Change color when off
    pygame.draw.rect(screen, color, (1130,90, 100, 30))  # Button rectangle
    text = font.render("Texture: ON" if show_textures else "Texture: OFF", True, WHITE)
    screen.blit(text, (1135, 98))

def draw_button_3(screen):
    # """Draws the toggle trail and reset zoom buttons."""
    # Trail Toggle Button
        trail_color = (100, 100, 100) if show_trails else (50, 50, 50)
        pygame.draw.rect(screen, trail_color, (1130, 130,100, 30))
        text = font.render("Trails: ON" if show_trails else "Trails: OFF", True, WHITE)
        screen.blit(text, (1135, 138))
    
def draw_button_4(screen):
     # Reset Zoom Button
        pygame.draw.rect(screen, (100, 100, 255), (1130, 170, 100, 30))
        text = font.render("Reset View", True, WHITE)
        screen.blit(text, (1135, 178))

def draw_button_5(screen):
     # Reset Zoom Button
        # Trail Toggle Button
        moon_color = (100, 100, 100) if show_moon else (50, 50, 50)
        pygame.draw.rect(screen, moon_color, (1130, 210,100, 30))
        text = font.render("Moon: ON" if show_trails else "Moon: OFF", True, WHITE)
        screen.blit(text, (1135, 218))