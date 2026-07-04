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
        # cria janela do jogo
        self.tela = Tela()
        self.width = config.LARGURA_TELA
        self.height = config.ALTURA_TELA
        # estado do jogo
        self.run = True # enquanto for True, o jogo não acaba 
        self.mudar_x = 0.0 # direção/velocidade atuais da nave
        self.background = None 
        self.player = None
        self.hazard = None
        self.placar = None

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
    
    #verifica a sobreposição do player e do hazard
    def _houve_colisao(self, player, hazard):
        return player.get_rect().colliderect(hazard.get_rect())
    
    # cria os objetos da partida
    def _inicializar_jogo(self):
        self.background = Background()
        self.player = Player()
        self.placar = Placar()
        # sorteia a posição do primeiro hazard
        h_x = random.randrange(config.SPAWN_MIN, config.SPAWN_MAX)
        self.hazard = criar_hazard(0, h_x, config.HAZARD_Y_INICIAL)

    # atualiza o estado do jogo por frame
    def _atualizar(self):
        self.background.rolar()
        self.player.mover(self.mudar_x)
        self.hazard.cair()

        # quando o obstáculo sai da tela, cria outro no topo e o player pontua
        if self.hazard.y > self.height:
            h_x = random.randrange(config.SPAWN_MIN, config.SPAWN_MAX_RESPAWN)
            tipo = random.randint(0, len(config.IMAGENS_HAZARD) - 1)
            self.hazard = criar_hazard(tipo, h_x, 0 - config.TAM_HAZARD)
            self.placar.adicionar_ponto()

    # desenha os objetos na tela
    def _renderizar(self):
        self.background.draw(self.tela.screen) # fundo parado
        self.background.mover(self.tela.screen) # fundo em movimento
        self.player.desenhar(self.tela.screen)
        self.placar.desenhar(self.tela.screen)
        self.hazard.desenhar(self.tela.screen)
        self.tela.atualizar() # mostra o frame
    

    def _detectar_colisoes(self):
        # Bater na lateral NÃO é fim de jogo: reaparece longe do hazard e continua
        if self.player.x > config.LIMITE_PLAYER_DIR or self.player.x < config.LIMITE_PLAYER_ESQ:
            self.tela.desenhar_mensagem(self.tela.msg_colisao)
            self.tela.atualizar()
            time.sleep(3)

            # coloca a nave no lado oposto ao hazard
            if self.hazard.x > self.width / 2:
                novo_x = self.hazard.x - self.width / 2
            else:
                novo_x = self.hazard.x + self.width / 2

            # garante que o player fique na área permitida
            if novo_x < config.LIMITE_PLAYER_ESQ:
                novo_x = config.LIMITE_PLAYER_ESQ
            if novo_x > config.LIMITE_PLAYER_DIR:
                novo_x = config.LIMITE_PLAYER_DIR

            self.player.x = novo_x
            self.mudar_x = 0

        # bater no hazard É fim de jogo
        if self._houve_colisao(self.player, self.hazard):
            self._tratar_fim_de_jogo(self.tela.msg_game_over)

    # mostra a mensagem final e encerra loop
    def _tratar_fim_de_jogo(self, mensagem):
        self.tela.desenhar_mensagem(mensagem)
        self.tela.atualizar()
        time.sleep(3)
        self.run = False

    #loop que coordena atualização, desenho de objetos e colisões
    def loop(self):
        self._inicializar_jogo()
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(config.FPS)
            self.handle_events()
            self._atualizar()
            self._renderizar()
            self._detectar_colisoes()
   
