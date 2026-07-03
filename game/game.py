import pygame
import random
import time

import config.config as config

from background.background import Background
from player_hazard.player import Player
from player_hazard.hazard import criar_hazard
from game.tela import Tela
from game.placar import Placar


class Game:

    # movimento do Player
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT

    def __init__(self):

        """
        Inicializa a tela e o estado do jogo
        """

        self.tela = Tela()
        self.width = config.LARGURA_TELA
        self.height = config.ALTURA_TELA
        self.run = True
        self.mudar_x = 0.0
        self.background = None
        self.player = None
        self.hazard = None
        self.placar = None
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
        self.background.draw(self.tela.screen)
    
    def _houve_colisao(self, player, hazard):
        return player.get_rect().colliderect(hazard.get_rect())
    
    def loop(self):
        """
        Laço principal
        """

        # variáveis para movimento de Plano de Fundo/Background
        velocidade_background = config.VEL_FUNDO
        velocidade_hazard = config.VEL_HAZARD

        hzrd = 0
        h_x = random.randrange(config.SPAWN_MIN, config.SPAWN_MAX)
        deslocamento = pygame.math.Vector2(0, 0)

        # Criar o Plano de fundo
        self.background = Background()

        # Criar o Player
        self.player = Player((self.width - 56) / 2, self.height - 125)

        # Criar Harzard
        self.hazard = criar_hazard(hzrd, h_x, config.HAZARD_Y_INICIAL)

        # Criar Placar
        self.placar = Placar()

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()

        # assim iniciamos o loop principal do programa
        while self.run:

            dt = clock.tick(config.FPS)

            # Handle Input Events
            self.handle_events()

            # Atualiza Elementos
            self.elements_update(dt)

            # Desenha o background buffer
            self.elements_draw()

            # Adiciona movimento ao background
            self.background.mover(self.tela.screen, deslocamento)
            deslocamento.y = deslocamento.y + velocidade_background

            #se a imagem ultrapassar a extremidade da tela, move de volta
            if deslocamento.y > config.LIMITE_REINICIO_FUNDO:
                deslocamento.y = deslocamento.y - config.LIMITE_REINICIO_FUNDO

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            self.player.x = self.player.x + self.mudar_x

            # Mostrar Player
            self.player.desenhar(self.tela.screen)

            # Mostrar Placar
            self.placar.desenhar(self.tela.screen)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if self.player.x > config.LIMITE_PLAYER_DIR or self.player.x < config.LIMITE_PLAYER_ESQ:
                self.tela.desenhar_mensagem(self.tela.msg_colisao)
                self.tela.atualizar()
                time.sleep(3)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            self.hazard.y = self.hazard.y + (velocidade_hazard / 4)
            self.hazard.desenhar(self.tela.screen)
            self.hazard.y = self.hazard.y + velocidade_hazard

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if self.hazard.y > self.height:
                h_x = random.randrange(config.SPAWN_MIN, 650 - config.TAM_HAZARD)
                hzrd = random.randint(0, 4)
                self.hazard = criar_hazard(hzrd, h_x, 0 - config.TAM_HAZARD)
                # determinando quantos hazard passaram e a pontuação
                self.placar.adicionar_ponto()

            # restrições para o game over
            if self._houve_colisao(self.player, self.hazard):
                self.tela.desenhar_mensagem(self.tela.msg_game_over)
                self.tela.atualizar()
                time.sleep(3)
                self.run = False

            # atualizando a tela
            self.tela.atualizar()