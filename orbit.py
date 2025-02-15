from import_init import*
from settings import*
# Orbits
def draw_dashed_ellipse(surface, center, radius, color, a_scale=1.2, b_scale=0.8, dash_length=10, gap_length=5):
    for angle in range(0, 360, 15):
        start_x = center[0] + radius * math.cos(math.radians(angle)) * a_scale
        start_y = center[1] + radius * math.sin(math.radians(angle)) * b_scale
        end_x = center[0] + radius * math.cos(math.radians(angle + 10)) * a_scale
        end_y = center[1] + radius * math.sin(math.radians(angle + 10)) * b_scale
        pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), 1)
