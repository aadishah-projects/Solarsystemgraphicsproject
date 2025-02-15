from import_init import*
from settings import*

class InfoPanel:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.visible = False  # Show only when a planet is selected
        self.selected_planet = None

    def show(self, planet):
        self.selected_planet = planet
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, screen, font):
        if self.visible and self.selected_planet:
            pygame.draw.rect(screen, (50, 50, 50), self.rect)  # Panel background
            pygame.draw.rect(screen, (200, 200, 200), self.rect, 2)  # Border

            # Display Planet Info
            text_lines = [
                f"Name: {self.selected_planet.name}",
                f"Radius: {planet_data_actual[self.selected_planet.name]['Radius']} km",
                f"Orbit Radius: {planet_data_actual[self.selected_planet.name]['Orbit Radius']} km",
                f"Speed: {planet_data_actual[self.selected_planet.name]['Speed']:.2f} km/s"
                    ]
            for i, line in enumerate(text_lines):
                text = font.render(line, True, (255, 255, 255))
                screen.blit(text, (self.rect.x + 10, self.rect.y + 10 + i * 20))

planet_data_actual = {
    "Mercury": {
        "Radius": 2440,  # in km
        "Orbit Radius": 57910000,  # in km
        "Speed": 47.87  # in km/s
    },
    "Venus": {
        "Radius": 6052,
        "Orbit Radius": 108200000,
        "Speed": 35.02
    },
    "Earth": {
        "Radius": 6371,
        "Orbit Radius": 149600000,
        "Speed": 29.78
    },
    "Mars": {
        "Radius": 3389,
        "Orbit Radius": 227900000,
        "Speed": 24.13
    },
    "Jupiter": {
        "Radius": 69911,
        "Orbit Radius": 778500000,
        "Speed": 13.07
    },
    "Saturn": {
        "Radius": 58232,
        "Orbit Radius": 1433000000,
        "Speed": 9.69
    },
    "Uranus": {
        "Radius": 25362,
        "Orbit Radius": 2871000000,
        "Speed": 6.81
    },
    "Neptune": {
        "Radius": 24622,
        "Orbit Radius": 4495000000,
        "Speed": 5.43
    }
}