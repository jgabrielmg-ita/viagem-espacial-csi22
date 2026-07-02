import pygame
import random
import time

import config

from background.background import Background
from player import Player
from hazard import Hazard


class Game:
    screen = None
    screen_size = None
    width = config.LARGURA_TELA
    height = config.ALTURA_TELA
    run = True
    background = None
    player = None
    hazard_1 = hazard_2 = hazard_3 = hazard_4 = hazard_5 = None
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

    # handle_events()

    def elements_update(self, dt):
        self.background.update(dt)
    # elements_update()

    def elements_draw(self):
        self.background.draw(self.screen)
    # elements_draw()

    # Desenha o Player
    def draw_player (self, x, y):
        self.player.draw (self.screen, x, y)
    # draw_player()

    # Desenha Hazard
    def draw_hazard (self, hzrd, x, y):
        if hzrd == 0:
            self.hazard_1.draw(self.screen, x, y)
        elif hzrd == 1:
            self.hazard_2.draw(self.screen, x, y)
        elif hzrd == 2:
            self.hazard_3.draw(self.screen, x, y)
        elif hzrd == 3:
            self.hazard_4.draw(self.screen, x, y)
        elif hzrd == 4:
            self.hazard_5.draw(self.screen, x, y)
    # draw_hazard()

    # Define as posições dos objetos para criar o movimento
    def move_background (self, obj_movL_x, obj_movL_y, obj_movR_x, obj_movR_y):
        self.background.move (self.screen, obj_movL_x, obj_movL_y, obj_movR_x,obj_movR_y)
    # move_background()

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

        faixaA_x = 375
        faixaA_y = 0
        hzrd = 0
        h_x = random.randrange(config.SPAWN_MIN, config.SPAWN_MAX)
        h_y = config.HAZARD_Y_INICIAL

        # Info Hazard
        h_width = config.TAM_HAZARD  #55
        h_height = config.TAM_HAZARD #120

        # movimento da margem esquerda
        movL_x = 0
        movL_y = 0

        # movimento da margem direita
        movR_x = config.POS_MARGEM_DIR_X
        movR_y = 0

        # Criar o Plano de fundo
        self.background = Background()

        # Posicao do Player
        x = (self.width - 56) / 2
        y = self.height - 125

        # Criar o Player
        self.player = Player(x, y)

        # Criar Harzard_1
        self.hazard_1 = Hazard(config.IMAGENS_HAZARD[0], h_x, h_y)

        # Criar Harzard_2
        self.hazard_2 = Hazard(config.IMAGENS_HAZARD[1], h_x, h_y)

        # Criar Harzard_3
        self.hazard_3 = Hazard(config.IMAGENS_HAZARD[2], h_x, h_y)

        # Criar Harzard_4
        self.hazard_4 = Hazard(config.IMAGENS_HAZARD[3], h_x, h_y)

        # Criar Harzard_5
        self.hazard_5 = Hazard(config.IMAGENS_HAZARD[4], h_x, h_y)

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

            # adiciona movimento ao background

            self.move_background (movL_x, movL_y, movR_x, movR_y)
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background

            #se a imagem ultrapassar a extremidade da tela, move de volta
            if movL_y > config.LIMITE_REINICIO_FUNDO and movR_y > config.LIMITE_REINICIO_FUNDO:
                movL_y -= config.LIMITE_REINICIO_FUNDO
                movR_y -= config.LIMITE_REINICIO_FUNDO

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            x = x + self.mudar_x

            # Mostrar Player
            self.draw_player (x, y)

            # Mostrar score
            self.score_card(self.screen, h_passou, score)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if x > config.LIMITE_PLAYER_DIR or x < config.LIMITE_PLAYER_ESQ:
                self.screen.blit(self.render_text_bateulateral, config.POS_MENSAGEM)
                pygame.display.update()  # atualizar a tela
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            h_y = h_y + velocidade_hazard / 4
            self.draw_hazard(hzrd, h_x, h_y)
            h_y = h_y + velocidade_hazard

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if h_y > self.height:
                h_y = 0 - h_height
                faixaA_y = 0
                h_x = random.randrange(config.SPAWN_MIN, 650 - h_height)
                hzrd = random.randint(0, 4)
                # determinando quantos hazard passaram e a pontuação
                h_passou = h_passou + 1
                score = h_passou * config.PONTOS_POR_HAZARD

            # restrições para o game over
            if y < h_y + h_height:
                if x > h_x or x > h_x - 56:
                    if x < h_x + h_width or x < h_x - 56:
                        self.screen.blit(self.render_text_perdeu, config.POS_MENSAGEM)
                        pygame.display.update()
                        time.sleep(3)
                        self.run = False

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)

        # while self.run
    # loop()
# Game: