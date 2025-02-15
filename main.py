from import_init import*
from settings import*
from orbit import *
from planet import *
from button import *
from panel import *
from starrybg import *
from sun import *
from moon import *

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
pygame.display.set_caption("Solar System Simulation")


# Solar System Objects
sun = Planet("sun",640, 360, 30, SUN_COLOR, "assets/sun.png", 0, 0,2)
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]


planets = [
    Planet(planet_names[0],WIDTH // 2, HEIGHT // 2, 10, PLANET_COLORS[0], "assets/mercury.png", 60, 0.08,2),
    Planet(planet_names[1],WIDTH // 2, HEIGHT // 2, 12, PLANET_COLORS[1],"assets/venus.png", 110, 0.06,1.5),
    Planet(planet_names[2],WIDTH // 2, HEIGHT // 2, 14, PLANET_COLORS[2],"assets/earth.png", 160, 0.05,2),
    Planet(planet_names[3],WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[3],"assets/march.png", 210, 0.04,1),
    Planet(planet_names[4],WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[4],"assets/jupiter.png", 320, 0.02,1.5),
    Planet(planet_names[5],WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[5],"assets/saturn.png", 420, 0.015,2),
    Planet(planet_names[6],WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[6],"assets/neptune.png", 520, 0.01,1),
    Planet(planet_names[7],WIDTH // 2, HEIGHT // 2, 16, PLANET_COLORS[7],"assets/uranus.png", 600, 0.07,2.5)
]

moon_data = {
    "Earth": [(30, 4, (200, 200, 200), 0.1)],  # Moon
    "Jupiter": [
        (50, 5, (180, 180, 180), 0.05),  # Ganymede
        (40, 4, (150, 150, 150), 0.07),  # Europa
        (60, 3, (170, 170, 170), 0.03),  # Callisto
        (35, 2, (140, 140, 140), 0.09),  # Io
    ],
    "Saturn": [
        (45, 5, (190, 190, 190), 0.04),  # Titan
        (35, 3, (160, 160, 160), 0.06),  # Enceladus
        (30, 2, (140, 140, 140), 0.08),  # Mimas
    ],
}

def check_button_click(pos):
    global show_orbits
    global show_textures
    global show_trails, zoom_factor, pan_x, pan_y
    global show_moon
    button_x, button_y, button_width, button_height = 1130, 50, 100, 30  # Button position & size
    button_x_2, button_y_2, button_width_2, button_height_2 = 1130, 90, 100, 30  # Button position & size
    button_x_3, button_y_3, button_width_3, button_height_3 = 1130, 130, 100, 30  # Button position & size
    button_x_4, button_y_4, button_width_4, button_height_4 = 1130, 170, 100, 30  # Button position & size
    button_x_5, button_y_5, button_width_5, button_height_5 = 1130, 210, 100, 30  # Button position & size

    if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
        show_orbits = not show_orbits
    if button_x_2 <= pos[0] <= button_x_2 + button_width_2 and button_y_2 <= pos[1] <= button_y_2 + button_height_2:
        show_textures = not show_textures
    if button_x_3 <= pos[0] <= button_x_3 + button_width_3 and button_y_3 <= pos[1] <= button_y_3 + button_height_3:
        show_trails = not show_trails
    if button_x_4 <= pos[0] <= button_x_4 + button_width_4 and button_y_4 <= pos[1] <= button_y_4 + button_height_4:
        zoom_factor = 1.0
        pan_x, pan_y = 0, 0  # Reset position
    if button_x_5 <= pos[0] <= button_x_5 + button_width_5 and button_y_5 <= pos[1] <= button_y_5 + button_height_5:
        show_moon = not show_moon

def check_planet_click(pos, planets, panel):
    for planet in planets:
        dist = math.sqrt((pos[0] - planet.x) ** 2 + (pos[1] - planet.y) ** 2)
        if dist < planet.radius:  # If click is inside the planet
            panel.show(planet)
            return
    panel.hide()  # Hide panel if clicked elsewhere

clock = pygame.time.Clock()
FPS = 144
info_panel = InfoPanel(850, 50, 250, 150)

# Main loop
running = True
while running:
    screen.fill(BLACK)
    draw_starry_background(screen)  # Draw stars
      # Draw sun flare
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Press 'O' to toggle orbits
            if event.key == pygame.K_o:
                show_orbits = not show_orbits

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll Up (Zoom In)
                zoom_factor *= 1.1
            elif event.button == 5:  # Scroll Down (Zoom Out)
                zoom_factor /= 1.1
            elif event.button == 1:  # Left Click (Start Dragging)
                dragging = True
                last_mouse_pos = pygame.mouse.get_pos()
                check_button_click(pygame.mouse.get_pos())
                check_planet_click(pygame.mouse.get_pos(), planets, info_panel)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left Click Release (Stop Dragging)
                dragging = False
        
        elif event.type == pygame.MOUSEMOTION and dragging:
        # 🖱️ Calculate Mouse Drag Distance
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - last_mouse_pos[0]
            dy = mouse_y - last_mouse_pos[1]

            pan_x += dx
            pan_y += dy
            last_mouse_pos = (mouse_x, mouse_y)  # Update last position
    
    
    # sun.draw(screen)
    if show_textures:
        draw_textures_sun(screen,sun_texture, zoom_factor, pan_x, pan_y)
    else :     
        draw_sun(screen,zoom_factor, pan_x, pan_y)
    
    moons = []

    for planet in planets:
        if planet.name in moon_data:
            for moon_info in moon_data[planet.name]:
                orbit_radius, size, color, speed = moon_info
                moons.append(Moon(planet, orbit_radius, size, color, speed))

    for i, planet in enumerate(planets):
        planet.update_position(zoom_factor, pan_x, pan_y)

        if show_trails:
            planet.draw_trail(screen,zoom_factor, pan_x, pan_y)
        if show_orbits:
            draw_dashed_ellipse(screen, (WIDTH // 2, HEIGHT // 2), planet.orbit_radius, WHITE)
        
        if show_textures:
            planet.draw_textures(screen,zoom_factor,pan_x,pan_y)
        else:
            planet.draw(screen,zoom_factor, pan_x, pan_y)

        planet.draw_label(screen, planet_names[i])
        
        if show_moon:
            for moon in moons:
                moon.update_position()
                moon.draw_orbit(screen, zoom_factor, pan_x, pan_y)  # Draw orbit path
                moon.draw(screen, zoom_factor, pan_x, pan_y)  # Draw the moon
        
    # Draw info panel if visible
    info_panel.draw(screen, font)
    draw_button_1(screen)
    draw_button_2(screen)
    draw_button_3(screen)
    draw_button_4(screen)
    draw_button_5(screen)
        
    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
