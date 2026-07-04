import pygame

import config.config as config

class Player:
    """
    Classe Jogador
    """
    def __init__(self):
        #carrega e redimensiona a imagem da nave
        player_fig = pygame.image.load(config.IMG_PLAYER)
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (config.TAM_PLAYER, config.TAM_PLAYER))
        self.image = player_fig
        # posicão inicial centralizada na horizontal e com offset vertical da base
        self.x = self.x_central()
        self.y = config.ALTURA_TELA - config.OFFSET_PLAYER_Y

    # calcula o x que centraliza a nave na tela
    def x_central(self):
        return (config.LARGURA_TELA - config.DESLOC_CENTRO_PLAYER) / 2

    # move a nave dx pixels na direção x 
    def mover(self, dx):
        self.x = self.x + dx

    # desenha a nave na posição atual
    def desenhar(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    # Retorna o retângulo da nave para verificar colisão
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

# Player: