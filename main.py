from import_init import*
from settings import*
from orbit import *
from planet import *
from button import *

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
pygame.display.set_caption("Solar System Simulation")


# Solar System Objects
sun = Planet(640, 360, 30, SUN_COLOR, "assets/sun.png", 0, 0,2)
planets = [
    Planet(WIDTH // 2, HEIGHT // 2, 10, PLANET_COLORS[0], "assets/mercury.png", 60, 0.08,2),
    Planet(WIDTH // 2, HEIGHT // 2, 12, PLANET_COLORS[1],"assets/venus.png", 110, 0.06,1.5),
    Planet(WIDTH // 2, HEIGHT // 2, 14, PLANET_COLORS[2],"assets/earth.png", 160, 0.05,2),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[3],"assets/march.png", 210, 0.04,1),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[4],"assets/jupiter.png", 320, 0.02,1.5),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[5],"assets/saturn.png", 420, 0.015,2),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[6],"assets/neptune.png", 520, 0.01,1),
    Planet(WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[7],"assets/uranus.png", 600, 0.07,2.5)
]
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def check_button_click(pos):
    global show_orbits
    global show_textures
    button_x, button_y, button_width, button_height = 1130, 50, 100, 30  # Button position & size
    button_x_2, button_y_2, button_width_2, button_height_2 = 1130, 90, 100, 30  # Button position & size
    if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
        show_orbits = not show_orbits
    if button_x_2 <= pos[0] <= button_x_2 + button_width_2 and button_y_2 <= pos[1] <= button_y_2 + button_height_2:
        show_textures = not show_textures
  
def draw_textures_sun(screen):
    image = pygame.image.load("assets/sun.png")
    image = pygame.transform.scale(image, (2 *  30, 2 *  30))
    screen.blit(image, (int(640 -  30), int(360 -  30)))

clock = pygame.time.Clock()
FPS = 144
# Main loop
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
    if show_textures:
        draw_textures_sun(screen)
    else :     
        pygame.gfxdraw.filled_circle(screen, WIDTH // 2, HEIGHT // 2, 30, SUN_COLOR)
        pygame.gfxdraw.aacircle(screen, WIDTH // 2, HEIGHT // 2, 30, SUN_COLOR)
    
    for i, planet in enumerate(planets):
        
        if show_orbits:
            draw_dashed_ellipse(screen, (WIDTH // 2, HEIGHT // 2), planet.orbit_radius, WHITE)
        
        planet.update_position()

        if show_textures:
            planet.draw_textures(screen)
        else:
            planet.draw(screen)
        
        planet.draw_label(screen, planet_names[i])
        draw_button_1(screen)
        draw_button_2(screen)
    # for planet in planets:
    #     planet.update_position()
    #     planet.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
