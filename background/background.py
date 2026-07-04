import pygame

import config.config as config

class Background:
    """
    Esta classe define o Plano de Fundo do jogo
    """
    def __init__(self):
        # carrega o fundo e as duas margens redimensionadas
        self.image = self._carregar(config.IMG_FUNDO)
        self.margin_left = self._carregar(config.IMG_MARGEM_ESQ, (config.LARGURA_MARGEM, config.ALTURA_MARGEM))
        self.margin_right = self._carregar(config.IMG_MARGEM_DIR, (config.LARGURA_MARGEM, config.ALTURA_MARGEM))

        # Vetor que guarda o quanto o fundo já rolou
        self.deslocamento = pygame.math.Vector2(0, 0)

    # Carrega uma imagem e, se um tamanho for dado, redimensiona
    def _carregar(self, caminho, tamanho=None):
        fig = pygame.image.load(caminho)
        fig.convert()
        if tamanho is not None:
            fig = pygame.transform.scale(fig, tamanho)
        return fig

    # desenha o fundo e as margens na posição inicial
    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (config.POS_MARGEM_DIR_X, 0))

    # desenha imagem repetidamente até cobrir toda a tela
    def _desenhar_coluna(self, screen, image, x, y):
        passo = config.ALTURA_BLOCO_FUNDO        # altura de um bloco (o "passo")
        pos = y
        while pos > 0 :                          # sobe até 'pos' cobrir/passar o topo
            pos -= passo
        while pos < config.ALTURA_TELA:        # desce cobrindo até a base da tela
            screen.blit(image, (x, pos))
            pos += passo

    # avança o deslocamento do fundo e reinicia quando passa do limite
    def rolar(self):
        self.deslocamento.y = self.deslocamento.y + config.VEL_FUNDO
        if self.deslocamento.y > config.LIMITE_REINICIO_FUNDO:
            self.deslocamento.y = self.deslocamento.y - config.LIMITE_REINICIO_FUNDO


    # Define posições do Plano de Fundo para criar o movimento
    def mover (self, screen):

        #movimento background
        self._desenhar_coluna(screen, self.image, 0, self.deslocamento.y)

        # movimento margem esquerda
        self._desenhar_coluna(screen, self.margin_left, 0, self.deslocamento.y)

        # movimento margem direita
        self._desenhar_coluna(screen, self.margin_right, config.POS_MARGEM_DIR_X, self.deslocamento.y)
