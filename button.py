from import_init import*
from settings import*
#button
def draw_button(screen):
    color = (100, 100, 100) if show_orbits else (50, 50, 50)  # Change color when off
    pygame.draw.rect(screen, color, (1130,50, 100, 30))  # Button rectangle
    text = font.render("Orbits: ON" if show_orbits else "Orbits: OFF", True, WHITE)
    screen.blit(text, (1135, 58))

