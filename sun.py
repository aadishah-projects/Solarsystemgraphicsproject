from import_init import*
from settings import*

sun_texture = pygame.image.load("assets/sun.png")
sun_texture = pygame.transform.scale(sun_texture, (2 *  30, 2 *  30))

def draw_textures_sun(screen,sun_texture, zoom_factor, pan_x, pan_y):
    # Adjust sun position for zoom and pan
    sun_x = (WIDTH // 2 - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
    sun_y = (HEIGHT // 2 - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
    sun_size = int(60 * zoom_factor)  # Adjust sun size dynamically

    # Scale texture
    scaled_sun = pygame.transform.smoothscale(sun_texture, (sun_size, sun_size))
    # Centered positioning
    rect = scaled_sun.get_rect(center=(int(sun_x), int(sun_y)))
    # Draw sun texture
    screen.blit(scaled_sun, rect.topleft)
    


def draw_sun(screen,zoom_factor, pan_x, pan_y):
    sun_x = (WIDTH // 2 - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
    sun_y = (HEIGHT // 2 - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
    sun_radius = int(30 * zoom_factor)  # Scale sun size
    # Draw sun with zoom
    pygame.gfxdraw.filled_circle(screen, int(sun_x), int(sun_y), sun_radius, SUN_COLOR)
    pygame.gfxdraw.aacircle(screen, int(sun_x), int(sun_y), sun_radius, SUN_COLOR)
