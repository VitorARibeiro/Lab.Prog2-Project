import pygame 
import os
#Nome Janela
pygame.display.set_caption('Senet')
#VARIAVEIS GLOBAIS
WIDTH, HEIGHT = 1000,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
COLOR_BG = (142,160,118)
MENU_BG = (142,160,118)
FPS = 60
BORDAX = 100
BORDAY = 100
CLOCK = pygame.time.Clock()

#IMAGENS 
Board_img = pygame.image.load(os.path.join('Assets','Board Senet.png'))
Peca_Preta_img = pygame.image.load(os.path.join('Assets','Triangulo_Preto.png'))
Peca_Branca_img = pygame.image.load(os.path.join('Assets','Circulo_Branco.png'))
Homem_Passaro_img = pygame.image.load(os.path.join('Assets','Homem_Passaro.png'))
Mulher_Egito_img = pygame.image.load(os.path.join('Assets','Mulher_Egito.png'))

#DEFINICAO DE FUNCOES




#funcao de posicao no tabuleiro em x e y            
def posicao_peca(posicao,peca):
    sequencia = [0,1,2,3,4,5,6,7,8,9,19,18,17,16,15,14,13,12,11,10,20,21,22,23,24,25,26,27,28,29] #sequencia de posicoes que a peca deve seguir
    peca.x = (sequencia[posicao] % 10 ) * 80 + BORDAX
    peca.y = (sequencia[posicao] // 10 ) * 80 + BORDAY   

#DRAW FUNCTIONS
def draw_Game(Board,Peca):
    WIN.fill(COLOR_BG)
    WIN.blit(Board_img,Board)

    for i in range(10):
        if i %2 == 0: #se peça for par é branca
            WIN.blit(Peca_Branca_img,Peca[i])
        else: #se peça for preta
            WIN.blit(Peca_Preta_img,Peca[i])

    pygame.display.update()

def draw_Menu(Botoes):
    WIN.fill(MENU_BG)
    WIN.blit(Mulher_Egito_img,(0,100))
    WIN.blit(Homem_Passaro_img,(700,150))
    for i in range(5):
        pygame.draw.rect(WIN,(0,0,0),Botoes[i])
    
    pygame.display.update()

#------------------MENUS E JOGO----------------------

def Main_Menu():
    #geracao de retangulos para 
    Posicao_rato = pygame.mouse.get_pos() #posicao do rato
    Botao_NJogo = pygame.Rect(300,155,400,90)
    Botao_carregar = pygame.Rect(300,250,400,90)
    Botao_descricao =  pygame.Rect(300,345,400,90)
    Botao_definicoes =  pygame.Rect(300,440,400,90)
    Botao_sair = pygame.Rect(300,535,400,90)
    Botoes = [Botao_NJogo,Botao_carregar,Botao_descricao,Botao_definicoes,Botao_sair]
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                run = False
        draw_Menu(Botoes)

        #main Loop  
         
#definição da funcao principal
def Game():
    #Geraçao de retangulos para jogo
    Board = pygame.Rect(BORDAX,BORDAY,800,240) #retangulo da board
    Peca = []
    for i in range (10):
        Peca.append(pygame.Rect (BORDAX,BORDAY,80,80))
        posicao_peca(i,Peca[i]) #definir automaticamente posicao da peça

    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                run = False
        #main loop  
       
        draw_Game(Board,Peca)
        
        
  
        


#RUN MAIN LOOP

Game()

pygame.quit()
