import pygame,os,random

pygame.init()

#Nome Janela
pygame.display.set_caption('Senet')
#VARIAVEIS GLOBAIS
WIDTH, HEIGHT = 1000,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
TEXT_COLOR = (243, 243, 251)
FPS = 60
BORDAX = 100
BORDAY = 160


#variaveis a guardar
Jogador = 0
lancamento = 0
lancamento_Passado = 0
Vetor_Posicoes_Pecas = [0,0,0,0,0,0,0,0,0,0]
lancamento_feito = False
settings = [0,0] # 0 - player  1 - bot
                # branco  preto
#-----

CLOCK = pygame.time.Clock()


SEQUENCIA =     [0,1,2,3,4,9,8,7,6,5,
                 10,11,12,13,14,15,16,17,18,19,
                 29,28,27,26,25,24,23,22,21,20,
                 30,31,32,33,34,35,36,37,38,39,
                 40,41,42,43,44,49,48,47,46,45]


#----IMAGENS 
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
Lancar_Varas_img = pygame.image.load(os.path.join('Assets','Lancar_varas.png'))
Board_lancamento_img = pygame.image.load(os.path.join('Assets','Board_lancamentos.png'))
Consola_Jogo_img = pygame.image.load(os.path.join('Assets','Consola_Jogo.png'))
mini_peca_preta = pygame.transform.scale_by(Peca_Preta_img,0.8)
mini_peca_branca = pygame.transform.scale_by(Peca_Branca_img,0.7)
Big_peca_preta = pygame.transform.scale_by(Peca_Preta_img,2)
Big_peca_branca = pygame.transform.scale_by(Peca_Branca_img,2)
Winning_Board= pygame.image.load(os.path.join('Assets','Winning_Board.png'))

#DEFINICAO DE FUNCOES

def savegame(jogador, lancamento, lancamento_Passado, Vetor_Posicao_Pecas):
    with open("savegame.txt", "w") as arquivo:
        arquivo.write(f"jogador: {jogador}\n")
        arquivo.write(f"lancamento: {lancamento}\n")
        arquivo.write(f"lancamento_Passado: {lancamento_Passado}\n")
        arquivo.write("Vetor_Posicao_Pecas:\n")
        for posicao in Vetor_Posicao_Pecas:
            arquivo.write(f"{posicao}\n")
jogador = "Vitor Ribeiro"
lancamento = 5
lancamento_passado = True
vetor_posicao_pecas = [1, 3, 5, 7, 9]

savegame('meujogo.txt', jogador, lancamento, lancamento_passado, vetor_posicao_pecas)






#funcao de lançamento de sticjs

def throw_sticks():
    global lancamento_feito
    jogadas = random.randint(1,5)
    lancamento_feito = True
    return jogadas
    #2 ou 3 passa-se ao adeversario else

def next_player():
     global Jogador,lancamento_Passado
     if lancamento_Passado == 2 or lancamento_Passado == 3:#se a jogada anterior foi 2 ou 3 avanca
        Jogador += 1

def new_game(Peca,Vetor_Pos):
    global Jogador
    for i in range (10): #gerar novo jogo
        Peca.append(pygame.Rect (0,0,80,80)) #gerar pecas no topo do ecra
        posicao_peca(i+10,Peca,Vetor_Pos,i) #definir automaticamente posicao da peça
    Jogador = random.randint(0,1)

#check por incremento
        
#check por posicao absoluta
def move_check(posicao,Vetor_Pos,index):
    global lancamento
    pode_mover = True
    if posicao<10 : #nao pode ir para zona superior
        return False
    elif Vetor_Pos[index] == 37 and lancamento != 3:
        return False
    elif Vetor_Pos[index] == 38 and lancamento != 2:
        return False

    else:
        for i in range(10):
            if Vetor_Pos[i] == posicao and index%2 == i%2 and i != index: #--------se tiverem na mesma posicao e mesma cor
                pode_mover = False
            elif Vetor_Pos[i] == posicao and i!= index and index%2 != i%2: #-----mesmo posicao e cor diferente
                #checkar vizinhanca--protecao aliada---
                for item_antes in Vetor_Pos:
                    if item_antes == Vetor_Pos[i]-1: #se encontrar peca com a mesma cor antes nao move
                        if  i%2 == Vetor_Pos.index(Vetor_Pos[i]-1) %2:
                            pode_mover = False
                for item_depois in Vetor_Pos:
                    if item_depois == Vetor_Pos[i]+1: #se encontrar peca com a mesma cor depois nao move
                        if  i%2 == Vetor_Pos.index(Vetor_Pos[i]+1) %2:
                            pode_mover = False
                #mesmo com cores diferentes, nestas casas nao podem ser comidas ---casa da beleza e vida---                
                if Vetor_Pos[i] == 24 or Vetor_Pos[i] == 35:
                    pode_mover=False
            else: #----------nao depende de cor-----------
                for item in Vetor_Pos:
                    if posicao == 36 and item == 24: 
                        pode_mover = False
        

    return pode_mover

def possivel_jogar(lancamento, Vetor_Pos, Jogador):
    pecas_brancas = [0,2,4,6,8]
    pecas_pretas = [1,3,5,7,9]

    Pode_Mover = False 

    if Jogador % 2 == 0: #pecas brancas
        for position in pecas_brancas:
            if move_check(Vetor_Pos[position] + lancamento,Vetor_Pos,position) or move_check(Vetor_Pos[position] - lancamento,Vetor_Pos,position):
                Pode_Mover = True
    else: #pecas brancas
        for position in pecas_pretas:
            if move_check(Vetor_Pos[position] + lancamento,Vetor_Pos,position) or move_check(Vetor_Pos[position] - lancamento,Vetor_Pos,position):
                Pode_Mover = True

    return Pode_Mover

    
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
    global lancamento,lancamento_Passado
    peca[index].x = (SEQUENCIA[posicao] % 10 ) * 80 + BORDAX
    peca[index].y = (SEQUENCIA[posicao] // 10 ) * 80 + BORDAY - 80
    Vetor_Pos[index] = posicao
    lancamento_Passado = lancamento
    next_player()
    lancamento = 0 

    
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
    global lancamento_feito
    posicao = Vetor_Pos[index] + incremento
    lancamento_feito = False

    if peca_nao_terminou_jogo(Vetor_Pos,index) and incremento!=0: #nao esta no fim

        if fim_check(incremento,Vetor_Pos,index):
            mover_fim(peca,Vetor_Pos,index)  

        elif comer_check(posicao,Vetor_Pos,index): #se for preciso comer uma peça
            comer_peca(posicao,peca,Vetor_Pos,index)
            
        elif posicao == 36:
            posicao_peca(24,peca,Vetor_Pos,index)
            
        else:
            posicao_peca(posicao,peca,Vetor_Pos,index)
                
def winning_check(Vetor_pos): #retorna 0 se branco ganhar e 1 se preto ganhar
    venceu_branco = True
    venceu_preto = True
    for i in range (10):
        if i % 2 == 0: #brancas
            if Vetor_pos[i] < 40:
                venceu_branco = False
        else:
            if Vetor_pos[i]<40:
                venceu_preto = False
    if venceu_branco:
        return 0
    elif venceu_preto:
        return 1

#DRAW FUNCTIONS
def draw_Game(Board,Peca,Sair,Lanca_Paus,text_lancamento):
    global Jogador
    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Board_img,Board)
    WIN.blit(Sair_Guardar_img,Sair)
    WIN.blit(Lancar_Varas_img,Lanca_Paus)
    WIN.blit(Board_lancamento_img,(725,570))
    WIN.blit(Consola_Jogo_img,(115,480))
    WIN.blit(text_lancamento,(764,595))

    if Jogador % 2 == 0: #pecas brancas
        WIN.blit(mini_peca_branca,(315,505))
    else:
        WIN.blit(mini_peca_preta,(315,505))


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

def draw_Winning_Screen (Sair,index):
    #definir fonte 
    font_Winner = pygame.font.Font(None, 70)
    text_Winner = font_Winner.render("Stuart",True,TEXT_COLOR)

    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Sair_img,Sair)
    WIN.blit(Winning_Board,(250,150))
    #print peca vencedora
    if index == 0: #peca branca
        WIN.blit(Big_peca_branca,(420,210))
    else: #peca preta
        WIN.blit(Big_peca_preta,(420,210))

    WIN.blit(text_Winner,(350,380))

    pygame.display.update()

def draw_Def_screen(Sair):

    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Sair_img,Sair)

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
                            run = False #load jogo
                        elif i == 2:
                            run = False #ajuda
                        elif i == 3:
                            Def_screen() #def
                        elif i == 4:
                            pygame.quit()
        draw_Menu(Botoes)
                        
#definição da funcao principal
def Game():
    #Geraçao de retangulos para jogo
    Board = pygame.Rect(BORDAX,BORDAY,800,240) #retangulo da board
    Sair = pygame.Rect(5,5,220,80)
    Lanca_Paus = pygame.Rect(675,480,210,80)
    Peca = []
    #texto no ecra
    font_lancamento = pygame.font.Font(None, 80)
    text_lancamento = font_lancamento.render(" ",True,TEXT_COLOR)
    #Globais
    global lancamento
    global Jogador
    global Vetor_Posicoes_Pecas
    global lancamento_feito 
    global settings
    #
    pecas_brancas = [0,2,4,6,8]
    pecas_pretas = [1,3,5,7,9]

    #gerar novo jogo
    new_game(Peca,Vetor_Posicoes_Pecas)

    run = True
    while run:
        
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        CLOCK.tick(FPS)
        #jogadas a fazer
        if lancamento != 0:
            text_lancamento = font_lancamento.render(str(lancamento),True,TEXT_COLOR)
        else:
            text_lancamento = font_lancamento.render(" ",True,TEXT_COLOR)

        #condicao de vitoria 0 branca 1 preta
        if winning_check(Vetor_Posicoes_Pecas) == 0:
            Winning_Screen (0)
        elif winning_check(Vetor_Posicoes_Pecas) == 1:
            Winning_Screen (1)
        #saber se ha jogadas possiveis ou nao, se nao houver avança auto

        if lancamento != 0 and possivel_jogar(lancamento,Vetor_Posicoes_Pecas,Jogador) == False:
            Jogador += 1 #avança para proximo jogador

        # ---Açoes bots
        if settings[Jogador%2] == 1: #significa que é o bot a jogar

            if lancamento_feito == False: #Bot lanca dados antes de jogar
                print ("lanca boot")

            if Jogador % 2 == 0 : #bot branco
                print("BOTTT BRANCOO") #jogada do bot
                
            elif Jogador % 2 == 1:  #Bot preto
                print("BOT PRETOOO")
                


        #---Acoes click (humanos)
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                pygame.quit()

            if  event.type == pygame.MOUSEBUTTONDOWN:
                #clicar nas pecas
               
                if pygame.mouse.get_pressed()[0]: #andar para a frente
                    if Jogador % 2 == 0 and settings[0] == 0: #pecas brancas e for um player
                        for position in pecas_brancas:
                            if Peca[position].collidepoint(Posicao_rato):
                                if move_check(lancamento + Vetor_Posicoes_Pecas[position],Vetor_Posicoes_Pecas,position):
                                    mover_peca_incremento(lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                   
                                elif move_check( Vetor_Posicoes_Pecas[position] - lancamento,Vetor_Posicoes_Pecas,position):
                                    mover_peca_incremento(-lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                    

                    elif Jogador %2 != 0 and settings [1] == 0:#pecas pretas e jogador
                        for position in pecas_pretas:
                            if Peca[position].collidepoint(Posicao_rato):
                                if move_check(lancamento + Vetor_Posicoes_Pecas[position],Vetor_Posicoes_Pecas,position):
                                    mover_peca_incremento(lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                    
                                elif move_check( Vetor_Posicoes_Pecas[position] - lancamento,Vetor_Posicoes_Pecas,position):
                                    mover_peca_incremento(-lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                    
                

                #clicar para lancar varas/paus 
                if Lanca_Paus.collidepoint(Posicao_rato) and lancamento_feito == False and settings[Jogador%2] == 0: # e se for player
                    lancamento = throw_sticks() #lanca paus e caso seja necessario avancar, avanca
                


                #clicar para sair
                if Sair.collidepoint(Posicao_rato):
                    Main_Menu()

       
        draw_Game(Board,Peca,Sair,Lanca_Paus,text_lancamento)

def Winning_Screen(index):
    #retangulos 
    Sair = pygame.Rect(5,5,220,80)
    

    run = True
    while run:
        CLOCK.tick(FPS)
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Sair.collidepoint(Posicao_rato):
                    Main_Menu()


        draw_Winning_Screen(Sair,index)
                
def Def_screen():
    Sair = pygame.Rect(5,5,220,80)
    

    run = True
    while run:
        CLOCK.tick(FPS)
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Sair.collidepoint(Posicao_rato):
                    Main_Menu()
        draw_Def_screen(Sair)

    
        
#RUN MAIN LOOP
Main_Menu()


pygame.quit()
