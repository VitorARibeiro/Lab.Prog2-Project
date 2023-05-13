import pygame,os,random,time

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
BOT_DELAY = 2

#variaveis a guardar && default values
Jogador = 0
lancamento = 0
lancamento_Passado = 0
Vetor_Posicoes_Pecas = [10,11,12,13,14,15,16,17,18,19]
lancamento_feito = False
settings = [0,0] # 0 - player  1 - bot
                # branco  preto
name_player0_text = "Sem Nome"
name_player1_text = "Sem Nome"

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
Bot_def= pygame.image.load(os.path.join('Assets','Bot_def.png'))
Humano_def= pygame.image.load(os.path.join('Assets','Humano_def.png'))
Red_button_def= pygame.image.load(os.path.join('Assets','Red_button.png'))
Green_button_def= pygame.image.load(os.path.join('Assets','Green_Button.png'))



#DEFINICAO DE FUNCOES
#funcao bot
def bot_branco(Peca,Vetor_Posicoes_Pecas):
    global Jogador
    pecas_brancas = [0,2,4,6,8]
    lista = []
    #escolher peca aleatoria e ver se é possivel mover

    for items in pecas_brancas:
        if Vetor_Posicoes_Pecas[items] < 40 and (move_check(lancamento + Vetor_Posicoes_Pecas[items],Vetor_Posicoes_Pecas,items) or move_check(Vetor_Posicoes_Pecas[items] - lancamento,Vetor_Posicoes_Pecas,items)):
            lista.append(items)
    if lista: #se tiver alguma jogada possivel, joga

        index = random.choice(lista)
        if move_check(lancamento + Vetor_Posicoes_Pecas[index],Vetor_Posicoes_Pecas,index):   
            mover_peca_incremento(lancamento,Peca,Vetor_Posicoes_Pecas,index)
        else:
            mover_peca_incremento(-lancamento,Peca,Vetor_Posicoes_Pecas,index)
        
    else:
        print("nao pode jogar, avanca")
   

def bot_preto(Peca,Vetor_Posicoes_Pecas):
    pecas_pretas = [1,3,5,7,9]
    global Jogador
    lista = []
    #escolher peca aleatoria e ver se é possivel mover

    for items in pecas_pretas:
        if Vetor_Posicoes_Pecas[items] < 40 and (move_check(lancamento + Vetor_Posicoes_Pecas[items],Vetor_Posicoes_Pecas,items) or move_check(Vetor_Posicoes_Pecas[items] - lancamento,Vetor_Posicoes_Pecas,items)):
            lista.append(items)
    if lista: #se tiver alguma jogada possivel, joga

        index = random.choice(lista)
        if move_check(lancamento + Vetor_Posicoes_Pecas[index],Vetor_Posicoes_Pecas,index):
            mover_peca_incremento(lancamento,Peca,Vetor_Posicoes_Pecas,index)
        else:
            mover_peca_incremento(-lancamento,Peca,Vetor_Posicoes_Pecas,index)
    else:
        print("nao pode jogar, avanca")
   

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
# load e new game
def new_game():
    global Jogador,lancamento ,lancamento_Passado,Vetor_Posicoes_Pecas,lancamento_feito
    Jogador = random.randint(1,2)
    lancamento = 0
    lancamento_Passado = 0
    Vetor_Posicoes_Pecas = [10,11,12,13,14,15,16,17,18,19]
    lancamento_feito = False
  
def Load_board(Peca,Vetor_Pos):
    global Jogador
    for i in range (10): #gerar novo jogo
        Peca.append(pygame.Rect (0,0,80,80)) #gerar pecas no topo do ecra
        posicao_peca(Vetor_Posicoes_Pecas[i],Peca,Vetor_Pos,i) #definir automaticamente posicao da peça

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
    elif posicao > 39: #fim do tabuleiro
        return True

    else:
        for i in range(10):
            if Vetor_Pos[i] == posicao and index%2 == i%2 and i != index: #--------se tiverem na mesma posicao e mesma cor
                pode_mover = False
            if Vetor_Pos[i] == posicao and i!= index and index%2 != i%2: #-----mesmo posicao e cor diferente
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
             #----------nao depende de cor-----------
        
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
            if Vetor_Pos[position] < 40 and (move_check(Vetor_Pos[position] + lancamento,Vetor_Pos,position) or move_check(Vetor_Pos[position] - lancamento,Vetor_Pos,position)):
                Pode_Mover = True
    else: #pecas pretas
        for position in pecas_pretas:
            if Vetor_Pos[position] < 40 and (move_check(Vetor_Pos[position] + lancamento,Vetor_Pos,position) or move_check(Vetor_Pos[position] - lancamento,Vetor_Pos,position)):
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
    global name_player0_text,name_player1_text
    #definir fonte 
    font_Winner = pygame.font.Font(None, 70)

    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Sair_img,Sair)
    WIN.blit(Winning_Board,(250,150))
    #print peca vencedora
    if index == 0 and settings[0] == 0: #pessoa peca branca
        WIN.blit(Big_peca_branca,(420,210))
        text_Winner = font_Winner.render(name_player0_text,True,TEXT_COLOR)
    elif index == 1 and settings[1] == 0: #pessoa peca preta
        WIN.blit(Big_peca_preta,(420,210))
        text_Winner = font_Winner.render(name_player1_text,True,TEXT_COLOR)
    elif index == 0 and settings[0] == 1: #bot peca branca
        WIN.blit(Big_peca_branca,(420,210))
        text_Winner = font_Winner.render("Bot_Branco",True,TEXT_COLOR)
    else: #bot peca preta
        WIN.blit(Big_peca_preta,(420,210))
        text_Winner = font_Winner.render("Bot_Preto",True,TEXT_COLOR)

    WIN.blit(text_Winner,(350,380))

    pygame.display.update()

def draw_Def_screen(Sair,Player_0_0,Player_0_1,Player_1_0,Player_1_1):

    # draw names---
    global name_player0_text,name_player1_text,settings
    name_font = pygame.font.Font(None,30)
    name_player0 = name_font.render(name_player0_text,True,TEXT_COLOR)
    name_player1 = name_font.render(name_player1_text,True,TEXT_COLOR)

    WIN.blit(BackGound_img,(0,0))
    WIN.blit(Sair_img,Sair)
    WIN.blit(Humano_def,Player_0_0)
    WIN.blit(Humano_def,Player_1_0)
    WIN.blit(Bot_def,Player_0_1)
    WIN.blit(Bot_def,Player_1_1)

    if settings[0] == 0: #player0 humano
        WIN.blit(Green_button_def,(73,280))
    elif settings[0] == 1: #player0 bot
        WIN.blit(Green_button_def,(73,560))
    if settings[1] == 0: #player0 humano
        WIN.blit(Green_button_def,(880,280))
    elif settings[1] == 1: #player0 bot
        WIN.blit(Green_button_def,(880,560))
    WIN.blit(name_player0,(250,325))
    WIN.blit(name_player1,(685,325))


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
                            new_game() #altera tabuleiro e random jogador
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

    #new game 
    Load_board(Peca,Vetor_Posicoes_Pecas)
    #primeiro desenho 
    draw_Game(Board,Peca,Sair,Lanca_Paus,text_lancamento)

    run = True
    while run:
        
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        CLOCK.tick(FPS)

        # ---Açoes bots
        if settings[Jogador%2] == 1: #significa que é o bot a jogar
            
            if lancamento_feito == False: #Bot lanca dados antes de jogar
                time.sleep(BOT_DELAY)
                lancamento = throw_sticks() #lanca paus e caso seja necessario avancar, avanca
                #atualizar lancamentos para bot 
                if lancamento != 0:
                    text_lancamento = font_lancamento.render(str(lancamento),True,TEXT_COLOR)
                else:
                    text_lancamento = font_lancamento.render(" ",True,TEXT_COLOR)
                
                draw_Game(Board,Peca,Sair,Lanca_Paus,text_lancamento)

                
            
                 
            if Jogador % 2 == 0 : #bot branco
                time.sleep(BOT_DELAY)
                bot_branco(Peca,Vetor_Posicoes_Pecas)
                
            elif Jogador % 2 == 1:  #Bot preto
                time.sleep(BOT_DELAY)
                bot_preto(Peca,Vetor_Posicoes_Pecas)

        #condicao de vitoria 0 branca 1 preta
        if winning_check(Vetor_Posicoes_Pecas) == 0:
            Winning_Screen (0)
        elif winning_check(Vetor_Posicoes_Pecas) == 1:
            Winning_Screen (1)
        #saber se ha jogadas possiveis ou nao, se nao houver avança auto

        if lancamento != 0 and not possivel_jogar(lancamento,Vetor_Posicoes_Pecas,Jogador):
            Jogador += 1 #avança para proximo jogador
            lancamento_feito = False
            print("avancou")

        


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

                                elif move_check(Vetor_Posicoes_Pecas[position] - lancamento,Vetor_Posicoes_Pecas,position):
                                    mover_peca_incremento(-lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                    

                    elif Jogador %2 != 0 and settings [1] == 0:#pecas pretas e jogador
                        for position in pecas_pretas:
                            if Peca[position].collidepoint(Posicao_rato):
                               
                                if move_check(lancamento + Vetor_Posicoes_Pecas[position],Vetor_Posicoes_Pecas,position) :
                                    mover_peca_incremento(lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                    
                                elif move_check( Vetor_Posicoes_Pecas[position] - lancamento,Vetor_Posicoes_Pecas,position) :
                                    mover_peca_incremento(-lancamento,Peca,Vetor_Posicoes_Pecas,position)
                                    
                

                #clicar para lancar varas/paus 
                if Lanca_Paus.collidepoint(Posicao_rato) and lancamento_feito == False and settings[Jogador%2] == 0: # e se for player
                    lancamento = throw_sticks() #lanca paus e caso seja necessario avancar, avanca
                


                #clicar para sair
                if Sair.collidepoint(Posicao_rato):
                    Main_Menu()

       
        #jogadas a fazer
        if lancamento != 0:
            text_lancamento = font_lancamento.render(str(lancamento),True,TEXT_COLOR)
        else:
            text_lancamento = font_lancamento.render(" ",True,TEXT_COLOR)

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
    global name_player1_text,name_player0_text,settings
    Sair = pygame.Rect(5,5,220,80)
    Player_0_0 = pygame.Rect(133,253,300,120)
    Player_0_1 = pygame.Rect(133,527,300,120)
    Player_1_0 = pygame.Rect(567,253,300,120)
    Player_1_1 = pygame.Rect(567,527,300,120)
    #box pressed

    player_0_0_status = False
    player_1_0_status = False
   
   
    
 
    run = True
    while run:
        CLOCK.tick(FPS)
        Posicao_rato = pygame.mouse.get_pos() #posicao do rato
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  #Fechar programa no X
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                player_0_0_status = False
                player_1_0_status = False

                if Sair.collidepoint(Posicao_rato):
                    Main_Menu()

                if Player_0_0.collidepoint(Posicao_rato):
                    settings[0] = 0
                    player_0_0_status = True
    
                if Player_0_1.collidepoint(Posicao_rato):
                    settings[0] = 1

                if Player_1_0.collidepoint(Posicao_rato):
                    settings[1] = 0
                    player_1_0_status = True

                if Player_1_1.collidepoint(Posicao_rato):
                    settings[1] = 1
               
            
            if event.type == pygame.KEYDOWN: #escrever no ecra
                if player_0_0_status:
                    if event.key == pygame.K_BACKSPACE:
                        name_player0_text = name_player0_text[:-1]
                    else:
                        name_player0_text += event.unicode
                elif player_1_0_status:
                    if event.key == pygame.K_BACKSPACE:
                        name_player1_text = name_player1_text[:-1]
                    else:
                        name_player1_text += event.unicode


        draw_Def_screen(Sair,Player_0_0,Player_0_1,Player_1_0,Player_1_1)

    
        
#RUN MAIN LOOP
Main_Menu()


pygame.quit()
