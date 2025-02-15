from import_init import*
from settings import*
# Orbits
def draw_dashed_ellipse(screen, center, radius, color, zoom_factor, pan_x, pan_y, ellipse_a=1.2, ellipse_b=0.8):
    """Draw a dashed ellipse with zoom, pan, and elliptical scaling."""
    # Adjust center for zoom and pan
    zoomed_center = (
        (center[0] - WIDTH // 2) * zoom_factor + WIDTH // 2 + pan_x,
        (center[1] - HEIGHT // 2) * zoom_factor + HEIGHT // 2 + pan_y
    )
    zoomed_radius_x = radius * ellipse_a * zoom_factor  # Scale x-axis
    zoomed_radius_y = radius * ellipse_b * zoom_factor  # Scale y-axis

    # Draw dashed ellipse
    num_segments = 100  # Number of segments for smoothness
    dash_length = 10  # Length of each dash
    gap_length = 5  # Length of each gap

    for i in range(0, num_segments, dash_length + gap_length):
        start_angle = 2 * math.pi * i / num_segments
        end_angle = 2 * math.pi * (i + dash_length) / num_segments

        # Draw a segment of the ellipse
        pygame.draw.arc(
            screen,
            color,
            (
                zoomed_center[0] - zoomed_radius_x,
                zoomed_center[1] - zoomed_radius_y,
                2 * zoomed_radius_x,
                2 * zoomed_radius_y
            ),
            start_angle,
            end_angle,
            1  # Line thickness
        )