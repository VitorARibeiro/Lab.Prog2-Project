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

SEQUENCIA =     [0,1,2,3,4,5,6,7,8,9,
                 10,11,12,13,14,15,16,17,18,19,
                 29,28,27,26,25,24,23,22,21,20,
                 30,31,32,33,34,35,36,37,38,39,
                 40,41,42,43,44,45,46,47,48,49]


#IMAGENS 
Board_img = pygame.image.load(os.path.join('Assets','Board Senet.png'))
Peca_Preta_img = pygame.image.load(os.path.join('Assets','Triangulo_Preto.png'))
Peca_Branca_img = pygame.image.load(os.path.join('Assets','Circulo_Branco.png'))
Homem_Passaro_img = pygame.image.load(os.path.join('Assets','Homem_Passaro.png'))
Mulher_Egito_img = pygame.image.load(os.path.join('Assets','Mulher_Egito.png'))
Senet_Logo_img = pygame.image.load(os.path.join('Assets','Senet_Logo.png'))
NJogo_img = pygame.image.load(os.path.join('Assets','NJogo_img.png'))
CJogo_img = pygame.image.load(os.path.join('Assets','CJogo_img.png'))
Ajuda_img = pygame.image.load(os.path.join('Assets','Ajuda_img.png'))
Definicoes_img = pygame.image.load(os.path.join('Assets','Definicoes_img.png'))
Sair_img = pygame.image.load(os.path.join('Assets','Sair.png'))
BackGound_img = pygame.image.load(os.path.join('Assets','BG.png'))


#DEFINICAO DE FUNCOES


#funcao de posicao no tabuleiro em x e y            
def posicao_peca(posicao,peca,Vetor_Pos,index): #digo em que posicao quero a peça
    peca.x = (SEQUENCIA[posicao] % 10 ) * 80 + BORDAX
    peca.y = (SEQUENCIA[posicao] // 10 ) * 80 + 20  
    Vetor_Pos[index] = posicao

def posicao_peca_incremento (incremento,peca,Vetor_Pos,index): #digo quanto quero que a peca avance
    posicao = Vetor_Pos[index] + incremento
    peca.x = (SEQUENCIA[posicao] % 10 ) * 80 + BORDAX
    peca.y = (SEQUENCIA[posicao] // 10 ) * 80 + 20  
    Vetor_Pos[index] = posicao



#DRAW FUNCTIONS
def draw_Game(Board,Peca):
    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Board_img,Board)

    for i in range(10):
        if i %2 == 0: #se peça for par é branca
            WIN.blit(Peca_Branca_img,Peca[i])
        else: #se peça for preta
            WIN.blit(Peca_Preta_img,Peca[i])

    pygame.display.update()

def draw_Menu(Botoes):
    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Mulher_Egito_img,(0,150))
    WIN.blit(Homem_Passaro_img,(700,200))
    WIN.blit(Senet_Logo_img,(300,30))
    #botoes---
    WIN.blit(NJogo_img,Botoes[0])
    WIN.blit(CJogo_img,Botoes[1])
    WIN.blit(Ajuda_img,Botoes[2])
    WIN.blit(Definicoes_img,Botoes[3])
    WIN.blit(Sair_img,Botoes[4])
    
    pygame.display.update()

#------------------MENUS E JOGO----------------------

def Main_Menu():
    #geracao de retangulos para 
    
    Botao_NJogo = pygame.Rect(375,155,250,90)
    Botao_carregar = pygame.Rect(375,250,250,90)
    Botao_descricao =  pygame.Rect(375,345,250,90)
    Botao_definicoes =  pygame.Rect(375,440,250,90)
    Botao_sair = pygame.Rect(375,535,250,90)
    Botoes = [Botao_NJogo,Botao_carregar,Botao_descricao,Botao_definicoes,Botao_sair]
    run = True
    while run:
        CLOCK.tick(FPS)
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                pygame.quit()

        #main Loop  
        draw_Menu(Botoes)
        for i in range(5):
            
            if Botoes[i].collidepoint(Posicao_rato) and pygame.mouse.get_pressed()[0]:
                
                if i == 0:
                    Game() #inicia Jogo
                elif i == 1:
                    run = False
                elif i == 2:
                    run = False
                elif i == 3:
                    run = False
                elif i == 4:
                    run = False #Sair
                

         
#definição da funcao principal
def Game():
    #Geraçao de retangulos para jogo
    Board = pygame.Rect(BORDAX,BORDAY,800,240) #retangulo da board
    Peca = []
    Vetor_Posicoes_Pecas = [0,0,0,0,0,0,0,0,0,0]
    for i in range (10):
        Peca.append(pygame.Rect (0,0,80,80)) #gerar pecas no topo do ecra
        posicao_peca(i+10,Peca[i],Vetor_Posicoes_Pecas,i) #definir automaticamente posicao da peça

    run = True
    while run:
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        CLOCK.tick(FPS)
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                pygame.quit()
        #main loop  
        for i in range (10):
            if Peca[i].collidepoint(Posicao_rato) and pygame.mouse.get_pressed()[0]:
                posicao_peca_incremento(1,Peca[i],Vetor_Posicoes_Pecas,i)
                print(Vetor_Posicoes_Pecas)
                if i % 2 == 0: #peca par
                    print("clicou na peca Branca index -> ",i)
                else:
                    print("clicou na peca Preta index -> ",i)

       
        draw_Game(Board,Peca)
        
        
  
        


#RUN MAIN LOOP
Game()


pygame.quit()
