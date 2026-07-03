import pygame

import config.config as config

class Tela:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.LARGURA_TELA, config.ALTURA_TELA))
        pygame.mouse.set_visible(0)
        pygame.display.set_caption(config.TITULO_JANELA)

        fonte = pygame.font.Font(config.FONTE_TITULO, config.TAM_FONTE_TITULO)
        self.msg_colisao = fonte.render("COLISÃO!", 0, config.BRANCO)
        self.msg_game_over = fonte.render("GAME OVER!", 0, config.VERMELHO)

    def desenhar_mensagem(self, mensagem):
        self.screen.blit(mensagem, config.POS_MENSAGEM)

    def atualizar(self):
        pygame.display.update()      