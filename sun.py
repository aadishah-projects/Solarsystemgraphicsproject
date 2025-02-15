from import_init import*
from settings import*

# def draw_sun_flare(screen, x, y, max_radius=200):
#     """Draws a sun flare with a fading glow effect."""
#     for i in range(max_radius, 0, -5):  # Decrease radius to create layers
#         alpha = int(255 * (i / max_radius))  # Fades outward
#         flare_color = (255, 204, 0, alpha)  # Yellowish glow
#         flare_surface = pygame.Surface((2 * i, 2 * i), pygame.SRCALPHA)
#         pygame.draw.circle(flare_surface, flare_color, (i, i), i)
#         screen.blit(flare_surface, (x - i, y - i), special_flags=pygame.BLEND_RGB_ADD)

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
    # draw_sun_flare(screen, sun_x, sun_y)
    # Draw sun texture
    screen.blit(scaled_sun, rect.topleft)
    


def draw_sun(screen,zoom_factor, pan_x, pan_y):
    sun_x = (WIDTH // 2 - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x
    sun_y = (HEIGHT // 2 - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
    sun_radius = int(30 * zoom_factor)  # Scale sun size
    # draw_sun_flare(screen, sun_x, sun_y)
    # Draw sun with zoom
    pygame.gfxdraw.filled_circle(screen, int(sun_x), int(sun_y), sun_radius, SUN_COLOR)
    pygame.gfxdraw.aacircle(screen, int(sun_x), int(sun_y), sun_radius, SUN_COLOR)
