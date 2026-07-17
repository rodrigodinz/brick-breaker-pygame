import pygame

#Inicializar
pygame.init() #inicia o programa

tamanho_tela = (800, 800) #tamanho da tela
tela = pygame.display.set_mode(tamanho_tela) #cria a tela

pygame.display.set_caption("Brick Breaker") #nome do jogo

# Configurações do elemento do jogo
# Aqui você basicamente tem que criar todos os elementos que terão no jogo
# No caso do jogo brick breaker, temos a bola, temos o jogador (que é aquela) barra horizontal que fica na parte de baixo da tela, nós temos os blocos que ficam na parte de cima da tela e nós temos a pontuação que é o placar do jogo, que vai aumentando conforme o jogador vai acertando os blocos com a bola
# Além disso, também criamos a variável que controla o inicio e o fim do jogo, a lógica de quando o jogo começa ou termina virá depois, por enquanto essa variável será apenas de True ou False (Ou o jogo está rodanndo ou não)

#=========================BOLA=======================

tamanho_bola = 15 #tamanho da bola

bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola) #Aqui estamos apenas criando um retangulo, depois vamos colocar ele na tela
#Rect = retangulo

#=========================JOGADOR=======================

tamanho_jogador = 100 #tamanho do jogador

jogador = pygame.Rect(0, 750, tamanho_jogador, 15) #Aqui estamos apenas criando um retangulo que é o jogador, depois vamos colocar ele na tela

#=========================JOGO=======================

tamanho_blocos = 75 #tamanho dos blocos

qtde_blocos_linha = 8
qtde_linhas = 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas

cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "vermelho": (255, 0, 0),
    "amarelo": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0),
}

def criar_blocos(qtde_blocos_linha, qtde_linhas):
    #A função da função é criar os blocos do jogo, que são os alvos da bola, e devolver uma lista com todos os blocos criados
    blocos = [] #cria os blocos
    return blocos

fim_jogo = False # Variável para controlar o fim do jogo
pontuacao = 0
movimento_bola = [1, 1]  # Velocidade da bola (x, y) - Ela se movimenta 1 pixel para a direita e 1 pixel para baixo a cada atualização

# Criar as funções do jogo



# Desenhar as coisas na tela
def desenhar_inicio_jogo():

    tela.fill(cores["preto"]) #preenche a tela com a cor preta
    #Pega a variavel da tela (que tem um tamanho) e preenche (fill) com uma cor estabelecida na matriz de cores do programa

    pygame.draw.rect(tela, cores["azul"], jogador) #Desenha o jogador na tela
    #A sintaxe é onde, como (que cor) e o que. Nesse caso, na tela, com a cor azul e sendo a variável do tamanho jogador
    pygame.draw.rect(tela, cores["branco"], bola)

desenhar_inicio_jogo()

# Criar um loop infinito

while not fim_jogo:
    for evento in pygame.event.get(): #Captura qualquer tipo de interação do usuário com o jogo, como apertar uma tecla, clicar com o mouse, etc
        if evento.type == pygame.QUIT: #Se o usuário clicar no X da tela, o jogo fecha
            fim_jogo = True #Se o usuário clicar no X da tela, o jogo fecha,
        

    pygame.time.wait(1) #A cada um milisegundo, a tela atualiza os comandos do jogo
    pygame.display.flip() #Atualiza a tela do jogo a cada mudança que acontece

pygame.quit() #Encerra o programa
