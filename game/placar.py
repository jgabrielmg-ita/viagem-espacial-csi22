import pygame

import config.config as config

class Placar:
    def __init__(self):
        self.h_passou = 0
        self.score = 0

    def adicionar_ponto(self):
        self.h_passou = self.h_passou + 1
        self.score = self.h_passou * config.PONTOS_POR_HAZARD

    def desenhar(self, screen):
        font = pygame.font.SysFont(None, config.TAM_FONTE_PLACAR)
        passou = font.render("Passou: " + str(self.h_passou), True, config.AMARELO_PASSOU)
        score = font.render("Score: " + str(self.score), True, config.AMARELO_SCORE)
        screen.blit(passou, config.POS_TEXTO_PASSOU)
        screen.blit(score, config.POS_TEXTO_SCORE)  

         