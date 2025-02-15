from import_init import*
from settings import*
from orbit import *
from planet import *
from button import *

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
pygame.display.set_caption("Solar System Simulation")


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



def check_button_click(pos):
    global show_orbits
    button_x, button_y, button_width, button_height = 1130, 50, 100, 30  # Button position & size
    
    if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
        show_orbits = not show_orbits

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
