import pygame

import config.config as config

class Player:
    """
    Classe Jogador
    """
    def __init__(self):
        player_fig = pygame.image.load(config.IMG_PLAYER)
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (config.TAM_PLAYER, config.TAM_PLAYER))
        self.image = player_fig
        self.x = self.x_central()
        self.y = config.ALTURA_TELA - config.OFFSET_PLAYER_Y

    def x_central(self):
        return (config.LARGURA_TELA - config.DESLOC_CENTRO_PLAYER) / 2

    def mover(self, dx):
        self.x = self.x + dx

    # Desenhar o Player
    def desenhar(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    # Retorna a posicao do Player
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

# Player: