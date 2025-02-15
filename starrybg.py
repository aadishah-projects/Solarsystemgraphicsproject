from import_init import*
from settings import*
import random
from bg import *
# Generate random star positions
NUM_STARS = 300  # Adjust for more or fewer stars
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

def draw_parallax_background(screen, pan_x, pan_y):
    # Parallax effect: Background moves slower than planets
    parallax_x = -pan_x * 0.5   # Adjust factor for depth effect
    parallax_y = -pan_y * 0.5

    # Wrap-around effect
    bg_x = parallax_x % galaxy_bg.get_width()
    bg_y = parallax_y % galaxy_bg.get_height()

    # Draw the background twice for smooth looping
    for i in range(-1, 2):  
        for j in range(-1, 2):  
            screen.blit(galaxy_bg, (bg_x + i * galaxy_bg.get_width(), bg_y + j * galaxy_bg.get_height()))
    # screen.blit(galaxy_bg, (bg_x - galaxy_bg.get_width(), bg_y - galaxy_bg.get_height()))
    # screen.blit(galaxy_bg, (bg_x, bg_y))