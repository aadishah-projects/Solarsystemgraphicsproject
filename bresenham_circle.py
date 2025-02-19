import pygame

# Bresenham's Circle Drawing Algorithm
def bresenham_circle(screen, color, xc, yc, r):
    x = r
    y = 0
    p = 3 - 2 * r  # Initial decision parameter

    # Draw points for all octants
    while x >= y:
        # 8 symmetrical points in each octant of the circle
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        screen.set_at((xc + y, yc + x), color)
        screen.set_at((xc - y, yc + x), color)
        screen.set_at((xc + y, yc - x), color)
        screen.set_at((xc - y, yc - x), color)

        # Update the decision parameter and coordinates
        y += 1

        if p <= 0:
            p = p + 4 * y + 6  # Decision parameter update
        else:
            x -= 1
            p = p + 4 * (y - x) + 10  # Decision parameter update

# Main function to set up Pygame and call the drawing function
def main():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((400, 400))

    # Set the color for the circle (Red)
    color = (255, 0, 0)

    # Circle parameters
    xc = 200  # X center
    yc = 200  # Y center
    r = 100  # Radius

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Draw the circle using Bresenham's algorithm
        bresenham_circle(screen, color, xc, yc, r)

        # Update the screen
        pygame.display.flip()

    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()
