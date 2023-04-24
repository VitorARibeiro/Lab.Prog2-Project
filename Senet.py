import pygame,os,random

#Nome Janela
pygame.display.set_caption('Senet')
#VARIAVEIS GLOBAIS
WIDTH, HEIGHT = 1000,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
COLOR_BG = (142,160,118)
MENU_BG = (142,160,118)
FPS = 60
BORDAX = 100
BORDAY = 160
CLOCK = pygame.time.Clock()

SEQUENCIA =     [0,1,2,3,4,9,8,7,6,5,
                 10,11,12,13,14,15,16,17,18,19,
                 29,28,27,26,25,24,23,22,21,20,
                 30,31,32,33,34,35,36,37,38,39,
                 40,41,42,43,44,49,48,47,46,45]


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
Sair_Guardar_img = pygame.image.load(os.path.join('Assets','Sair_Guardar.png'))


#DEFINICAO DE FUNCOES

#funcao de lançamento de sticjs
def throw_sticks():
    jogadas = random.randint(1,5)
    print(jogadas)
    return jogadas
    #2 ou 3 passa-se ao adeversario else
def new_game(Peca,Vetor_Pos):
    for i in range (10): #gerar novo jogo
        Peca.append(pygame.Rect (0,0,80,80)) #gerar pecas no topo do ecra
        posicao_peca(i+10,Peca,Vetor_Pos,i) #definir automaticamente posicao da peça

#check por incremento
        
#check por posicao absoluta
def move_check(posicao,Vetor_Pos,index):
    pode_mover = True
    if posicao<10: #nao pode ir para zona superior
        return False
    else:
        for i in range(10):
            if Vetor_Pos[i] == posicao and index%2 == i%2 and i != index: #se tiverem na mesma posicao e mesma cor
                pode_mover = False
        return pode_mover

def comer_check(posicao,Vetor_Pos,index):
    pode_comer = False
    for i in range(10):
            if Vetor_Pos[i] == posicao and index%2 != i%2 and i != index: #se tiverem cor diferente
                pode_comer = True
    return pode_comer

def comer_peca(posicao_final,peca,Vetor_Pos,index):
    pos_inicio = Vetor_Pos[index]
    for i in range(10):
        if Vetor_Pos[i] == posicao_final and i != index:
            final = i
    
    posicao_peca(posicao_final,peca,Vetor_Pos,index) #move peca inicial para a posicao final
    posicao_peca(pos_inicio,peca,Vetor_Pos,final) #move peca final para inicio
  
   
  
#funcao de posicao no tabuleiro em x e y            
def posicao_peca(posicao,peca,Vetor_Pos,index): #digo em que posicao quero a peça
    peca[index].x = (SEQUENCIA[posicao] % 10 ) * 80 + BORDAX
    peca[index].y = (SEQUENCIA[posicao] // 10 ) * 80 + BORDAY - 80
    Vetor_Pos[index] = posicao

    
def fim_check(incremento,Vetor_Pos,index): #checka se a peca vai sair do tabuleiro
    if Vetor_Pos[index] + incremento > 39:
        return True

def posicao_da_peca_fim(Vetor_Pos,index):#define em que posicao as pecas ficam no fim
    #descobrir se preta ou branca
    if index % 2 == 0: #peca branca
        for j in range(40,45):
            cond = True
            for i in range(10):
                if Vetor_Pos[i] == j:
                    cond = False
            if cond:
                return j
    else: #se a peça for preta
        for j in range(45,50):
            cond = True
            for i in range(10):
                if Vetor_Pos[i] == j:
                    cond = False
            if cond:
                return j

def mover_fim(peca,Vetor_Pos,index):
    posicao_peca(posicao_da_peca_fim(Vetor_Pos,index),peca,Vetor_Pos,index)
    
def peca_nao_terminou_jogo(Vetor_Pos,index):
    if Vetor_Pos[index]<40:
        return True
    

def mover_peca_incremento (incremento,peca,Vetor_Pos,index): #Logica principal do jogo
    posicao = Vetor_Pos[index] + incremento
    if peca_nao_terminou_jogo(Vetor_Pos,index): #nao esta no fim

        if fim_check(incremento,Vetor_Pos,index):
            mover_fim(peca,Vetor_Pos,index)
        else:
            if move_check(posicao,Vetor_Pos,index): #se for possivel mover a peca
                if comer_check(posicao,Vetor_Pos,index): #se for preciso comer uma peça
                    comer_peca(posicao,peca,Vetor_Pos,index)
                else:
                    posicao_peca(posicao,peca,Vetor_Pos,index)
    

#DRAW FUNCTIONS
def draw_Game(Board,Peca,Sair,Lanca_Paus):
    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Board_img,Board)
    WIN.blit(Sair_Guardar_img,Sair)
    pygame.draw.rect(WIN,(0,0,0),Lanca_Paus)


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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(5):
                    if Botoes[i].collidepoint(Posicao_rato):
                        
                        if i == 0:
                            Game() #inicia Jogo
                        elif i == 1:
                            run = False
                        elif i == 2:
                            run = False
                        elif i == 3:
                            run = False
                        elif i == 4:
                            pygame.quit()
        draw_Menu(Botoes)
                        
#definição da funcao principal
def Game():
    #Geraçao de retangulos para jogo
    Board = pygame.Rect(BORDAX,BORDAY,800,240) #retangulo da board
    Sair = pygame.Rect(5,5,220,80)
    Lanca_Paus = pygame.Rect(625,480,220,80)
    Peca = []
    Vetor_Posicoes_Pecas = [0,0,0,0,0,0,0,0,0,0]
    #gerar novo jogo
    new_game(Peca,Vetor_Posicoes_Pecas)
    

    run = True
    while run:
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        CLOCK.tick(FPS)
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                pygame.quit()

            if  event.type == pygame.MOUSEBUTTONDOWN:
                #clicar nas pecas
                for i in range (10):
                    if Peca[i].collidepoint(Posicao_rato):
                        print("colidida")
                        mover_peca_incremento(throw_sticks(),Peca,Vetor_Posicoes_Pecas,i)
                        break

                #clicar para sair
                if Sair.collidepoint(Posicao_rato):
                    Main_Menu()

       
        draw_Game(Board,Peca,Sair,Lanca_Paus)
        
        
#RUN MAIN LOOP
Main_Menu()


pygame.quit()
