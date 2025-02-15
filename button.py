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

