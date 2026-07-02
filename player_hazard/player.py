import pygame

import config.config as config

class Player:
    """
    Classe Jogador
    """
    image = None
    x = None
    y = None

    def __init__(self, x, y):
        player_fig = pygame.image.load(config.IMG_PLAYER)
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (config.TAM_PLAYER, config.TAM_PLAYER))
        self.image = player_fig
        self.x = x
        self.y = y
    # __init__()

    # Desenhar Player
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))
    #draw()
# Player: