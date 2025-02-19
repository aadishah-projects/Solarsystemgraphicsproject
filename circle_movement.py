import pygame

# Function to move the circle by a given velocity
def move_circle(xc, yc, velocity_x, velocity_y, width, height):
    # Update the center of the circle based on velocity
    xc += velocity_x
    yc += velocity_y
    
    # Prevent the circle from moving out of bounds
    if xc - width < 0 or xc + width > 400:
        velocity_x = -velocity_x  # Reverse direction on X-axis
    if yc - height < 0 or yc + height > 400:
        velocity_y = -velocity_y  # Reverse direction on Y-axis
    
    return xc, yc, velocity_x, velocity_y

# Main function to set up Pygame and call the drawing function
def main():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((400, 400))

    # Set the color for the circle (Red)
    color = (255, 0, 0)

    # Circle parameters
    xc = 100  # X center of the circle
    yc = 100  # Y center of the circle
    radius = 50  # Radius of the circle

    # Velocity (speed) of the circle in X and Y directions
    velocity_x = 2  # Move 2 pixels per frame in X direction
    velocity_y = 2  # Move 2 pixels per frame in Y direction

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Move the circle by updating its center position
        xc, yc, velocity_x, velocity_y = move_circle(xc, yc, velocity_x, velocity_y, radius, radius)

        # Draw the circle at the new position
        pygame.draw.circle(screen, color, (xc, yc), radius)

        # Update the screen
        pygame.display.flip()

        # Control the frame rate (for smoother animation)
        pygame.time.Clock().tick(60)

    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()
