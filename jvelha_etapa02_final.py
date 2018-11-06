# Exercício Final - AV em Grupo
##
##  RAFAEL MACHADO PEREIRA .
##  ROBERTO XAVIER DOS SANTOS .
##  TATIANE TONET LUGLI .

#JOGO DA VELHA

#FUNÇÕES
def Ftabuleiro():   #Exibe o tabuleiro atual
    Flinha()
    print("A seguir, o tabuleiro atualizado.\n")
    for i in range(3):
        print(tabuleiro[i])

def Flinha():   #Exibe uma linha
    print("=-"*32)

def Fposicao(jogador): #Exibe mensagem de Posição Utilizada
    print("{}, esta posição já foi utlizada, por favor digite outra posição.".format(jogador))

def Fjogador1(jogador):
    resp = int(input("{}, em qual posição você gostaria de marcar? ".format(jogador)))
    Flinha()

    #Verifica se o número digitado está entre as posições possíveis
    while resp < 1 or resp > 9:
        resp = int(input("{}, somente posições entre 1 a 9. ".format(jogador)))
        Ftabuleiro()

    #Marca "1" na posição digitada caso a mesma esteja vazia
    if resp in range(1,10):
        if resp == 1 and tabuleiro[0][0] == " ":
            tabuleiro[0][0] = "1"
        elif resp == 2 and tabuleiro[0][1] == " ":
            tabuleiro[0][1] = "1"
        elif resp == 3 and tabuleiro[0][2] == " ":
            tabuleiro[0][2] = "1"
        elif resp == 4 and tabuleiro[1][0] == " ":
            tabuleiro[1][0] = "1"
        elif resp == 5 and tabuleiro[1][1] == " ":
            tabuleiro[1][1] = "1"
        elif resp == 6 and tabuleiro[1][2] == " ":
            tabuleiro[1][2] = "1"
        elif resp == 7 and tabuleiro[2][0] == " ":
            tabuleiro[2][0] = "1"
        elif resp == 8 and tabuleiro[2][1] == " ":
            tabuleiro[2][1] = "1"
        elif resp == 9 and tabuleiro[2][2] == " ":
            tabuleiro[2][2] = "1"
        else:
            Fposicao(jogador)
            Ftabuleiro()
            Fjogador1(jogador)
    Ftabuleiro()
    Flinha()
    return "1"

def Fjogador2(jogador):
    resp = int(input("{}, em qual posição você gostaria de marcar? ".format(jogador)))
    Flinha()

    #Verifica se o número digitado está entre as posições possíveis
    while resp < 1 or resp > 9:
        resp = int(input("{}, somente posições entre 1 a 9. ".format(jogador)))
        Ftabuleiro()
    #Marca "2" na posição digitada caso a mesma esteja vazia
    if resp in range(1,10):
        if resp == 1 and tabuleiro[0][0] == " ":
            tabuleiro[0][0] = "2"
        elif resp == 2 and tabuleiro[0][1] == " ":
            tabuleiro[0][1] = "2"
        elif resp == 3 and tabuleiro[0][2] == " ":
            tabuleiro[0][2] = "2"
        elif resp == 4 and tabuleiro[1][0] == " ":
            tabuleiro[1][0] = "2"
        elif resp == 5 and tabuleiro[1][1] == " ":
            tabuleiro[1][1] = "2"
        elif resp == 6 and tabuleiro[1][2] == " ":
            tabuleiro[1][2] = "2"
        elif resp == 7 and tabuleiro[2][0] == " ":
            tabuleiro[2][0] = "2"
        elif resp == 8 and tabuleiro[2][1] == " ":
            tabuleiro[2][1] = "2"
        elif resp == 9 and tabuleiro[2][2] == " ":
            tabuleiro[2][2] = "2"
        else:
            Fposicao(jogador)
            Ftabuleiro()
            Fjogador2(jogador)
    Ftabuleiro()
    Flinha()
    return "2"

#DEFINIÇÕES
tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]

#CÓDIGO
print("Bem vindo ao Jogo da Velha.")
print("Vamos começar?\n")
jogador1 = input('JOGADOR 01, digite seu nome: ')
jogador2 = input('JOGADOR 02, digite seu nome: ')
Flinha()
print("A seguir, o mapa de casas do tabuleiro.")
for i in range(3):
    print(tabuleiro[i])
tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
cont = 0
for c in range(5):
    j1 = Fjogador1(jogador1)
    cont += 1
    j2 = Fjogador2(jogador2)
    cont += 1
