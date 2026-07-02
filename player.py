import pygame


class Player:
    """
    Classe Jogador
    """
    image = None
    x = None
    y = None

    def __init__(self, x, y):
        player_fig = pygame.image.load("Images/player.png")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.image = player_fig
        self.x = x
        self.y = y
    # __init__()

    # Desenhar Player
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))
    #draw()
# Player: