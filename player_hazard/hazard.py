import pygame

import config.config as config


class Hazard:
    def __init__(self, img, x, y):
        #carrega e redimensiona a image do obstáculo
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig, (config.TAM_HAZARD, config.TAM_HAZARD))
        self.image = hazard_fig
        self.x = x
        self.y = y

    # desce o hazard pela tela
    def cair(self):
        # velocidade efetiva 
        self.y = self.y + config.VEL_HAZARD

    # desenha o obstáculo na posição atual
    def desenhar (self, screen):
        screen.blit(self.image, (self.x, self.y))

    # retorna o retângulo do obstáculo para verificar colisão depois
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

# cria hazard a partir do índice da lista de imagens
def criar_hazard(tipo, x, y):
    return Hazard(config.IMAGENS_HAZARD[tipo], x, y)
