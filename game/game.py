import pygame
import random
import time

import config.config as config

from background.background import Background
from player_hazard.player import Player
from player_hazard.hazard import criar_hazard


class Game:
    screen = None
    screen_size = None
    width = config.LARGURA_TELA
    height = config.ALTURA_TELA
    run = True
    background = None
    player = None
    hazard = None
    render_text_bateulateral = None
    render_text_perdeu = None

    # movimento do Player
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT
    mudar_x = 0.0

    def __init__(self, size, fullscreen):

        """
        Função que inicializa o pygame, define a resolução da tela,
        caption, e desabilita o mouse.
        """

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))  # tamanho da tela
        self.screen_size = self.screen.get_size()

        pygame.mouse.set_visible(0)
        pygame.display.set_caption(config.TITULO_JANELA)

        # fontes
        my_font = pygame.font.Font(config.FONTE_TITULO, config.TAM_FONTE_TITULO)

        # Mensagens para o jogador
        self.render_text_bateulateral = my_font.render("COLISÃO!", 0,config.BRANCO)  # ("texto", opaco/transparente 0/1, cor do texto)
        self.render_text_perdeu = my_font.render("GAME OVER!", 0, config.VERMELHO)  # ("texto, opaco/transparente 0/1, cor do texto)

    # init()

    def handle_events(self):
        """
        Trata o evento e toma a ação necessária.
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            # se clicar em qualquer tecla, entra no if
            if event.type == pygame.KEYDOWN:
                # se clicar na seta da esquerda, anda 3 para a esquerda no eixo x
                if event.key == self.ESQUERDA:
                    self.mudar_x = -config.VEL_PLAYER
                # se clicar na seta da direita, anda 3 para a direita no eixo x
                if event.key == self.DIREITA:
                    self.mudar_x = config.VEL_PLAYER

            # se soltar qualquer tecla, não faz nada
            if event.type == pygame.KEYUP:
                if event.key == self.ESQUERDA or event.key == self.DIREITA:
                    self.mudar_x = 0

    def elements_update(self, dt):
        self.background.update(dt)
    
    def elements_draw(self):
        self.background.draw(self.screen)
    
    def _houver_colisao(self, player, hazard):
        return player.get_rect().colliderect(hazard.get_rect())
    
    # Informa a quantidade de hazard que passaram e a Pontuação
    def score_card(self, screen, h_passou, score):
        font = pygame.font.SysFont(None, config.TAM_FONTE_PLACAR)
        passou = font.render("Passou: " + str(h_passou), True, config.AMARELO_PASSOU)
        score = font.render("Score: " + str(score), True, config.AMARELO_SCORE)
        screen.blit(passou, config.POS_TEXTO_PASSOU)
        screen.blit(score, config.POS_TEXTO_SCORE)
    #score_card()

    def loop(self):
        """
        Laço principal
        """
        score = 0
        h_passou = 0

        # variáveis para movimento de Plano de Fundo/Background
        velocidade_background = config.VEL_FUNDO
        velocidade_hazard = config.VEL_HAZARD

        hzrd = 0
        h_x = random.randrange(config.SPAWN_MIN, config.SPAWN_MAX)
        h_y = config.HAZARD_Y_INICIAL

        deslocamento = pygame.math.Vector2(0, 0)
        # Criar o Plano de fundo
        self.background = Background()

        # Criar o Player
        self.player = Player((self.width - 56) / 2, self.height - 125)

        # Criar Harzard_1
        self.hazard = criar_hazard(hzrd, h_x, config.HAZARD_Y_INICIAL)

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = 16

        # assim iniciamos o loop principal do programa
        while self.run:
            clock.tick(1000 / dt)

            # Handle Input Events
            self.handle_events()

            # Atualiza Elementos
            self.elements_update(dt)

            # Desenha o background buffer
            self.elements_draw()

            # Adiciona movimento ao background
            self.background.mover(self.screen, deslocamento)
            deslocamento.y = deslocamento.y + velocidade_background

            #se a imagem ultrapassar a extremidade da tela, move de volta
            if deslocamento.y > config.LIMITE_REINICIO_FUNDO:
                deslocamento.y = deslocamento.y - config.LIMITE_REINICIO_FUNDO

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            self.player.x = self.player.x + self.mudar_x

            # Mostrar Player
            self.player.desenhar(self.screen)

            # Mostrar score
            self.score_card(self.screen, h_passou, score)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if self.player.x > config.LIMITE_PLAYER_DIR or self.player.x < config.LIMITE_PLAYER_ESQ:
                self.screen.blit(self.render_text_bateulateral, config.POS_MENSAGEM)
                pygame.display.update()  
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            self.hazard.y = self.hazard.y + (velocidade_hazard / 4)
            self.hazard.desenhar(self.screen)
            self.hazard.y = self.hazard.y + velocidade_hazard

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if self.hazard.y > self.height:
                h_x = random.randrange(config.SPAWN_MIN, 650 - config.TAM_HAZARD)
                hzrd = random.randint(0, 4)
                self.hazard = criar_hazard(hzrd, h_x, 0 - config.TAM_HAZARD)
                # determinando quantos hazard passaram e a pontuação
                h_passou = h_passou + 1
                score = h_passou * config.PONTOS_POR_HAZARD

            # restrições para o game over
            if self._houver_colisao(self.player, self.hazard):
                        self.screen.blit(self.render_text_perdeu, config.POS_MENSAGEM)
                        pygame.display.update()
                        time.sleep(3)
                        self.run = False

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)