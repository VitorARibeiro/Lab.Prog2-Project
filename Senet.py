import pygame 
import os

#VARIAVEIS GLOBAIS
WIDTH, HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
COLOR_BG = (212, 201, 133)
COLOR_BOARD = (235, 216, 103)
FPS = 60
BORDAX = 100
BORDAY = 100

#DEFINICAO DE FUNCOES




#funcao de posicao no tabuleiro em x e y            
def posicao_peca(posicao,peca):
    sequencia = [0,1,2,3,4,5,6,7,8,9,19,18,17,16,15,14,13,12,11,10,20,21,22,23,24,25,26,27,28,29] #sequencia de posicoes que a peca deve seguir
    peca.x = ( sequencia[posicao] % 10 ) * 80 + BORDAX
    peca.y = ( sequencia[posicao] // 10  ) * 80 + BORDAY   

#draw window
def draw_window(Board,Peca):
    WIN.fill(COLOR_BG)
    pygame.draw.rect(WIN,COLOR_BOARD,Board) #substituir por Win.blit com imagem no fim
    for i in range(10):
        if i %2 == 0: #se peça for par é branca
            pygame.draw.rect(WIN,(255,255,255),Peca[i])
        else:
            pygame.draw.rect(WIN,(0,0,0),Peca[i])



    
    pygame.display.update()


#definição da funcao principal
def main():
    Board = pygame.Rect(BORDAX,BORDAY,800,240) #retangulo da board
    Peca = []
    for i in range (10):
        Peca.append(pygame.Rect (BORDAX,BORDAY,80,80))
        posicao_peca(i,Peca[i]) #definir automaticamente posicao da peça

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #Fechar programa no X
            if event.type == pygame.QUIT:
                run = False
        #main loop  
       
        
        draw_window(Board,Peca)
        

    pygame.quit()


#RUN MAIN LOOP
main()
