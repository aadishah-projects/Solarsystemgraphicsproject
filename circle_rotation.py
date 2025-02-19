import pygame
import math

# Function to rotate a point around a given center
def rotate_point(x, y, xc, yc, angle):
    angle_rad = math.radians(angle)
    x -= xc
    y -= yc
    x_new = xc + (x * math.cos(angle_rad) - y * math.sin(angle_rad))
    y_new = yc + (x * math.sin(angle_rad) + y * math.cos(angle_rad))
    return (int(x_new), int(y_new))

# Main function to set up Pygame and animate rotation
def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    # Circle properties
    xc, yc = 200, 200  # Circle center
    radius = 50        # Circle radius
    angle = 0          # Rotation angle

    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear screen
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the circle
        pygame.draw.circle(screen, (255, 0, 0), (xc, yc), radius, 2)

        # Marker position (point at the top of the circle)
        marker_x, marker_y = xc, yc - radius

        # Rotate the marker around the circle
        rotated_x, rotated_y = rotate_point(marker_x, marker_y, xc, yc, angle)

        # Draw the rotating marker
        pygame.draw.line(screen, (0, 0, 255), (xc, yc), (rotated_x, rotated_y), 2)

        # Update rotation angle
        angle += 2  # Adjust for speed
        if angle >= 360:
            angle = 0

        pygame.display.flip()
        clock.tick(60)  # Control frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
