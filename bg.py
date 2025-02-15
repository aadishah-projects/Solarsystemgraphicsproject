from import_init import*
from settings import*
# Load background image
galaxy_bg = pygame.image.load("assets/bg.jpg")
galaxy_bg = pygame.transform.scale(galaxy_bg, (WIDTH * 2, HEIGHT * 2))  # Scale to be larger than the screen
