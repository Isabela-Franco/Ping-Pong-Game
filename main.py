import pygame
import random

#Iniciar 
pygame.init()

LARGURA, ALTURA = 530, 650
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Ping Pong Game')

#Cores
FUNDO = (20, 20, 30)
RAQUETE_JOGADOR_COR = (0, 200, 255)
RAQUETE_IA_COR = (255, 80, 80)
BOLA_COR = (255, 255, 255)
LINHA = (100, 100, 100)
FONTE = (240, 240, 240)
FONTE_PONTOS = (255, 255, 255)


raquete_largura, raquete_altura = 100, 15
raquete_jogador = pygame.Rect(LARGURA // 2 - (raquete_largura // 2), ALTURA - 20, raquete_largura, raquete_altura)
raquete_ia = pygame.Rect(LARGURA // 2 - (raquete_largura // 2), 5, raquete_largura, raquete_altura)
bola = pygame.Rect(LARGURA // 2 - 10, ALTURA // 2 - 10, 20, 20)

#Velocidade
vel_raquete = 7
vel_raquete_ia = 4
vel_bola_x = 5 * random.choice((1, -1))
vel_bola_y = 5 * random.choice((1, -1))

#Pontos
pontos_ia = 0
pontos_jogador = 0
fonte = pygame.font.Font(None, 60) 

clock = pygame.time.Clock()

#Loop
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Moviento jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] and raquete_jogador.left > 0 :
        raquete_jogador.x -= vel_raquete
    elif teclas[pygame.K_d] and raquete_jogador.right < LARGURA:
        raquete_jogador.x += vel_raquete

    #Movimento IA
    if vel_bola_y < 0:
        if raquete_ia.centerx < bola.centerx and raquete_ia.right < LARGURA:
            raquete_ia.x += vel_raquete_ia
        elif raquete_ia.centerx > bola.centerx and raquete_ia.left > 0:
            raquete_ia.x -= vel_raquete_ia

    #Movimento da bola
    bola.x += vel_bola_x
    bola.y += vel_bola_y

    #Colisões
    if bola.left <= 0 or  bola.right >= LARGURA:
        vel_bola_x *= -1

    if bola.colliderect(raquete_jogador) and vel_bola_y > 0:
        vel_bola_y *= -1

    if bola.colliderect(raquete_ia) and vel_bola_y < 0:
        vel_bola_y *= -1


    #Pontos
    if bola.top <= 0:
        pontos_jogador += 1
        bola.center = (LARGURA // 2, ALTURA // 2)
        vel_bola_x *= random.choice((1, -1))
        vel_bola_y *= random.choice((1, -1))

    if bola.top >= ALTURA:
        pontos_ia += 1
        bola.center = (LARGURA // 2, ALTURA // 2)
        vel_bola_x *= random.choice((1, -1))
        vel_bola_y *= random.choice((1, -1))

    TELA.fill(FUNDO)
    pygame.draw.line(TELA, LINHA, (0, ALTURA // 2), (LARGURA, ALTURA // 2), 3)
    pygame.draw.rect(TELA, RAQUETE_JOGADOR_COR, raquete_jogador, border_radius=8)
    pygame.draw.rect(TELA, RAQUETE_IA_COR, raquete_ia, border_radius=8)
    pygame.draw.ellipse(TELA, BOLA_COR, bola)

    pontos_txt_jogador = fonte.render(str(pontos_jogador), True, FONTE_PONTOS)  
    pontos_txt_ia = fonte.render(str(pontos_ia), True, FONTE_PONTOS)
    TELA.blit(pontos_txt_ia, (LARGURA // 2 - pontos_txt_ia.get_width() // 2, 80))  
    TELA.blit(pontos_txt_jogador, (LARGURA // 2 - pontos_txt_jogador.get_width() // 2, ALTURA - 120))  

            
    clock.tick(60)
    pygame.display.flip()