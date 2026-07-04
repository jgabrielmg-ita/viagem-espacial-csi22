from game.game import Game

# ponto de entrada do jogo
def main():
    # Cria o objeto game e chama o loop 
    game = Game()
    game.loop()

if __name__ == '__main__':
    main()