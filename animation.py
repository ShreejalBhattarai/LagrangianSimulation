import pygame
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant
dS2M = 1.496e11  # Distance from Sun to Earth in meters

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((1020, 800))
pygame.display.set_caption("Lagrange Points Simulation with Images")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class CelestialBody:
    def __init__(self, image_path, scale):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.position = np.array([0.0, 0.0])
        self.velocity = np.array([0.0, 0.0])

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


class Sun(CelestialBody):
    def __init__(self):
        super().__init__('32px-O.sun.png', (200, 200))
        self.position = np.array([400.0, 300.0])
        self.rect.center = self.position


class Earth(CelestialBody):
    def __init__(self):
        super().__init__('earth.png', (50, 50))
        self.position = np.array([400.0 + dS2M / 1e9, 300.0])
        self.rect.center = self.position


class Shuttle:
    def __init__(self):
        self.radius = 5
        self.color = RED
        self.position = np.array([100.0, 100.0])
        self.dragging = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.radius)


# Create objects
sun = Sun()
earth = Earth()
shuttle = Shuttle()




# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if np.linalg.norm(shuttle.position - np.array(event.pos)) < shuttle.radius:
                shuttle.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            shuttle.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if shuttle.dragging:
                shuttle.position = np.array(event.pos)

    # Clear screen
    screen.fill(BLACK)


    # Movement mechanics
    rect = pygame.Rect(200, 100, 400, 400)
    pygame.draw.ellipse(screen, WHITE, rect, 2)


    # Update positions
    earth.rect.center = earth.position
    sun.rect.center = sun.position

    # Draw Sun and Earth
    sun.draw(screen)
    earth.draw(screen)

    # Draw Shuttle
    shuttle.draw(screen)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
