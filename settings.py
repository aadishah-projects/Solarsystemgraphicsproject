from import_init import*
from settings import*
# Constants
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_COLOR = (255, 204, 0)
PLANET_COLORS = [(169, 169, 169),(255, 223, 186),(0, 102, 204),(255, 77, 77),(204, 153, 102),(255, 204, 102),(173, 216, 230),(0, 0, 128)]
show_orbits = True  # Initially, orbits are visible
font = pygame.font.Font(None, 24)  # Default font, size 24