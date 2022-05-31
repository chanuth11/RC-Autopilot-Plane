import pygame
import time
import math

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((760, 575))
        pygame.display.set_caption("Plane Visualizer")

        self.icon = pygame.image.load(r'globe.png')
        pygame.display.set_icon(self.icon)

        self.logo = pygame.image.load(r'logo.png')
        logo = pygame.transform.scale(self.logo, (140, 120))

        self.b2 = pygame.image.load(r'b2.png')
        self.b2 = pygame.transform.scale(self.b2, (760, 600))

        plane_art = pygame.image.load(r'plane.png')

        self.t0 = time.time()  # starts time

    def display_stat(self, stat, pos_x, pos_y):
        font = pygame.font.Font('freesansbold.ttf', 15)
        display = font.render(str(stat), True, 'white')
        return self.screen.blit(display, ((pos_x), (pos_y)))
    def background(self):
        self.screen.fill((5, 14, 57))
    def update(self):
        t1 = time.time()
        time_elapsed = t1 - self.t0
        c1 = time_elapsed % 50

        pygame.draw.circle(self.screen, 'green', (260, 267), 255)
        # pygame.draw.circle(screen, 'blue', (630,410), 100)
        pygame.draw.circle(self.screen, 'blue', (260, 267), 250)

        rect = (10, 17, 600, 500)
        self.screen.blit(self.b2, (0, 0))
    
        rect = (10, 17, 600, 500)
        self.screen.blit(self.b2, (0, 0))

        pygame.draw.line(self.screen, 'red', (252, 259), (268, 275), 5)
        pygame.draw.line(self.screen, 'red', (252, 275), (268, 259), 5)

        pygame.draw.line(self.screen, 'black', (10, 267), (510, 267), 3)
        pygame.draw.line(self.screen, 'black', (260, 17), (260, 517), 3)

        sinx = int(math.sin(time_elapsed) * 250)
        cosx = int(math.cos(time_elapsed) * 250)

        pygame.draw.line(self.screen, 'green', (260, 267), (260 + cosx, 267 + sinx), 1)

        for x in range(11):
            pygame.draw.line(self.screen, 'black', (10 + (50 * x), 260), (10 + (50 * x), 274), 2)
            pygame.draw.line(self.screen, 'black', (253, 17 + (50 * x)), (267, 17 + (50 * x)), 2)

        pygame.draw.line(self.screen, 'black', (10, 267), (510, 267), 2)

        