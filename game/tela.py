import pygame

import config.config as config

class Tela:
    def __init__(self):
        # inicializa pygame e cria a janela do jogo
        pygame.init()
        self.screen = pygame.display.set_mode((config.LARGURA_TELA, config.ALTURA_TELA))
        pygame.mouse.set_visible(0) # esconde cursor do mouse
        pygame.display.set_caption(config.TITULO_JANELA) # título da janela

        # prepara as mensagens da tela
        fonte = pygame.font.Font(config.FONTE_TITULO, config.TAM_FONTE_TITULO)
        self.msg_colisao = fonte.render("COLISÃO!", 0, config.BRANCO)
        self.msg_game_over = fonte.render("GAME OVER!", 0, config.VERMELHO)

    # desenha mensagem 
    def desenhar_mensagem(self, mensagem):
        self.screen.blit(mensagem, config.POS_MENSAGEM)

    # atualiza a tela, mostrando o que foi desenhado no frame
    def atualizar(self):
        pygame.display.update()      