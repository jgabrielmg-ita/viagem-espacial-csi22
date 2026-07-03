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
    def desenhar (self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))
    
# Hazard:

def criar_hazard(tipo, x, y):
    return Hazard(config.IMAGENS_HAZARD[tipo], x, y)
