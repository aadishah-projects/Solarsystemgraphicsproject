from import_init import*
from settings import*
import random

# Generate random star positions
NUM_STARS = 300  # Adjust for more or fewer stars
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

def draw_starry_background(screen):
    """Draws a starry background."""
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 1)  # Small white dots as stars