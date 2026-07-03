import pygame

import config.config as config

class Player:
    """
    Classe Jogador
    """
    def __init__(self, x, y):
        player_fig = pygame.image.load(config.IMG_PLAYER)
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (config.TAM_PLAYER, config.TAM_PLAYER))
        self.image = player_fig
        self.x = x
        self.y = y

    # Desenhar o Player
    def desenhar(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    # Retorna a posicao do Player
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

# Player: