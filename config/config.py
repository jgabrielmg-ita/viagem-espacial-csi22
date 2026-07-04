# constantes para não haver números sem nome no código

#janela/tela
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_JANELA = "Viagem Espacial"

FPS = 30

# player
TAM_PLAYER = 90 # lado do sprite da nave
VEL_PLAYER = 3 # pixels por frame
DESLOC_CENTRO_PLAYER = 56 # usado pra centralizar a nave (largura do sprite)
OFFSET_PLAYER_Y = 125 # distância da nave até a base da tela

LIMITE_PLAYER_ESQ = 45 # x mínimo antes de bater na margem esquerda
LIMITE_PLAYER_DIR = 668 # x máximo antes de bater na margem direita

#hazard
TAM_HAZARD = 130 #lado do sprite de obstáculo
VEL_HAZARD = 7*5/4  # velocidade de queda         
HAZARD_Y_INICIAL = -500     # y de partida do primeiro hazard (acima da tela)
SPAWN_MAX_RESPAWN = 650 - TAM_HAZARD # x máximo ao reaparecer um novo hazar
SPAWN_MIN = 125             # x mínimo de surgimento de azard
SPAWN_MAX = 660         # x máximo de surgimento do primeiro obstáculo

#lista de imagens do hazard 
IMAGENS_HAZARD = [
    "Images/nave.png",
    "Images/satelite.png",
    "Images/cometa.png",
    "Images/planeta.png",
    "Images/ameaca.png",
]

# fundo e margens
VEL_FUNDO = 5     # velocidade de rolagem do plano de fundo          
LARGURA_MARGEM = 60         # largura das margens laterais
ALTURA_MARGEM = 600 # altura das margens laterais
POS_MARGEM_DIR_X = 740      #x onde  a margem direita é desenhada 
ALTURA_BLOCO_FUNDO = 600    # altura de um bloco de fundo
LIMITE_REINICIO_FUNDO = 640 # quando o deslocamento passa disso, reinicia

# path das imagens de cenário e nave
IMG_FUNDO       = "Images/background.png"
IMG_MARGEM_ESQ  = "Images/margin_1.png"
IMG_MARGEM_DIR  = "Images/margin_2.png"
IMG_PLAYER      = "Images/player.png"

# fontes
FONTE_TITULO      = "Fonts/Fonte4.ttf"
TAM_FONTE_TITULO  = 100     
TAM_FONTE_PLACAR  = 35      

#cores usadas
BRANCO        = (255, 255, 255) # COLISÂO!
VERMELHO      = (255, 0, 0) # GAME OVER!
AMARELO_PASSOU = (255, 255, 128) #Passou:
AMARELO_SCORE  = (253, 231, 32) #Score:

# pontuação
PONTOS_POR_HAZARD = 10 # pontos ganhos por obstáculo desviado

#posicionamento dos textos na tela
POS_MENSAGEM      = (80, 200)   
POS_TEXTO_PASSOU  = (0, 50)     
POS_TEXTO_SCORE   = (0, 100)    