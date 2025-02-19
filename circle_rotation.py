import pygame
import math

# Function to rotate a point around a given center
def rotate_point(x, y, xc, yc, angle):
    # Convert the angle to radians
    angle_rad = math.radians(angle)

    # Translate point to origin (subtract center)
    x -= xc
    y -= yc

    # Apply the rotation matrix
    x_new = xc + (x * math.cos(angle_rad) - y * math.sin(angle_rad))
    y_new = yc + (x * math.sin(angle_rad) + y * math.cos(angle_rad))

    return (x_new, y_new)

# Bresenham's Circle Drawing Algorithm with Rotation
def bresenham_circle(screen, color, xc, yc, r, angle):
    x = r
    y = 0
    p = 3 - 2 * r  # Initial decision parameter

    # Draw points for all octants with rotation
    while x >= y:
        # Rotate and draw 8 points for each octant
        for dx, dy in [(x, y), (-x, y), (x, -y), (-x, -y),
                        (y, x), (-y, x), (y, -x), (-y, -x)]:
            # Rotate the point
            rotated_x, rotated_y = rotate_point(xc + dx, yc + dy, xc, yc, angle)
            screen.set_at((int(rotated_x), int(rotated_y)), color)

        y += 1
        if p <= 0:
            p = p + 4 * y + 6
        else:
            x -= 1
            p = p + 4 * (y - x) + 10

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
    r = 100   # Radius

    # Rotation angle (in degrees)
    angle = 0

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Draw the rotated circle using Bresenham's algorithm
        bresenham_circle(screen, color, xc, yc, r, angle)

        # Increment the angle for rotation (rotate 1 degree per frame)
        angle += 1
        if angle >= 360:
            angle = 0  # Reset to 0 after a full rotation

        # Update the screen
        pygame.display.flip()

    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()
