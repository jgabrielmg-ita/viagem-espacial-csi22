import pygame

import config.config as config


class Hazard:
    def __init__(self, img, x, y):
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig, (config.TAM_HAZARD, config.TAM_HAZARD))
        self.image = hazard_fig
        self.x = x
        self.y = y
    # __init__()

    # Desenhar Hazard
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))
    #draw()
# Hazard: