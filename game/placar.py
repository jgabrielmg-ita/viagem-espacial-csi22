import pygame

import config.config as config

class Placar:
    def __init__(self):
        # contadores de obstáculos e de pontuaçao
        self.h_passou = 0
        self.score = 0

    # soma obstáculo desviado e calcula nova pontuaçaõ
    def adicionar_ponto(self):
        self.h_passou = self.h_passou + 1
        self.score = self.h_passou * config.PONTOS_POR_HAZARD

    # desenha quantos hazards o player passou e a pontuação atual
    def desenhar(self, screen):
        font = pygame.font.SysFont(None, config.TAM_FONTE_PLACAR)
        passou = font.render("Passou: " + str(self.h_passou), True, config.AMARELO_PASSOU)
        score = font.render("Score: " + str(self.score), True, config.AMARELO_SCORE)
        screen.blit(passou, config.POS_TEXTO_PASSOU)
        screen.blit(score, config.POS_TEXTO_SCORE)  
        
    # reseta os pontos após colidir com asteroides
    def reset(self):
        self.h_passou = -1
        self.score = 0

         