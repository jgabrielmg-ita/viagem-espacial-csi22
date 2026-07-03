import pygame

import config.config as config

class Background:
    """
    Esta classe define o Plano de Fundo do jogo
    """
    def __init__(self):

        background_fig = pygame.image.load(config.IMG_FUNDO)
        background_fig.convert()
        self.image = background_fig

        margin_left_fig = pygame.image.load(config.IMG_MARGEM_ESQ)
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (config.LARGURA_MARGEM, config.ALTURA_MARGEM))
        self.margin_left = margin_left_fig

        margin_right_fig = pygame.image.load(config.IMG_MARGEM_DIR)
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (config.LARGURA_MARGEM, config.ALTURA_MARGEM))
        self.margin_right = margin_right_fig
    # __init__()

    def update(self, dt):
        pass
    # update()

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (config.POS_MARGEM_DIR_X, 0))
    # draw()

    def _desenhar_coluna(self, screen, image, x, y):
        passo = config.ALTURA_BLOCO_FUNDO        # altura de um bloco (o "passo")
        pos = y
        while pos > 0 :                          # sobe até 'pos' cobrir/passar o topo
            pos -= passo
        while pos < config.ALTURA_TELA:        # desce cobrindo até a base da tela
            screen.blit(image, (x, pos))
            pos += passo
    # _desenhar_coluna()

    # Define posições do Plano de Fundo para criar o movimento
    def move (self, screen, movL_x, movL_y, movR_x, movR_y):

        #movimento background
        self._desenhar_coluna(screen, self.image, movL_x, movL_y)

        # movimento margem esquerda
        self._desenhar_coluna(screen, self.margin_left, movL_x, movL_y)

        # movimento margem direita
        self._desenhar_coluna(screen, self.margin_right, movR_x, movR_y)
    # move()
# Background: