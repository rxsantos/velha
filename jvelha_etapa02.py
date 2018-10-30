# Exercício Final - AV em Grupo
##
##  RAFAEL MACHADO PEREIRA .
##  ROBERTO XAVIER DOS SANTOS .
##  TATIANE TONET LUGLI .

#JOGO DA VELHA

#FUNÇÕES

def Ftabuleiro():   #Exibe o tabuleiro atual
    print("A seguir, o tabuleiro atualizado.\n")
    for linha in tabuleiro:
        for i in linha:
            print(i,end='  ')
        print()

def cls():
    os.system("clear")

def Fempate(cont): #Verifica se houve empate
    if cont == 9:
        return True


def Flinha():   #Exibe uma linha
    print("=-"*32)

def Ffimjogo(): #Exibe mensagem de Fim de Jogo
    print("************************FIM DE JOGO*****************************")

def Fposicao(jogador): #Exige mensagem de Posição Utilizada
    print("{}, esta posição já foi utlizada, por favor digite outra posição.".format(jogador))

def Fchecar(x):  #Faz a checagem de vencedor.
    #diagonal principal
    if tabuleiro[0][0] == x and tabuleiro[1][1] == x and tabuleiro[2][2] == x:
        Ffimjogo()
        return True
    #diagonal secundária
    elif tabuleiro[0][2] == x and tabuleiro[1][1] == x and tabuleiro [2][0] == x:
        Ffimjogo()
        return True
    #linha 01
    elif tabuleiro[0][0] == x and tabuleiro[0][1] == x and tabuleiro[0][2] == x:
        Ffimjogo()
        return True
    #linha 02
    elif tabuleiro[1][0] == x and tabuleiro[1][1] == x and tabuleiro[1][2] == x:
        Ffimjogo()
        return True
    #linha 03
    elif tabuleiro[2][0] == x and tabuleiro[2][1] == x and tabuleiro[2][2] == x:
        Ffimjogo()
        return True
    #coluna 01
    elif tabuleiro[0][0] == x and tabuleiro[1][0] == x and tabuleiro[2][0] == x:
        Ffimjogo()
        return True
    #coluna 02
    elif tabuleiro[0][1] == x and tabuleiro[1][1] == x and tabuleiro[2][1] == x:
        Ffimjogo()
        return True
    #coluna 03
    elif tabuleiro[0][2] == x and tabuleiro[1][2] == x and tabuleiro[2][2] == x:
        Ffimjogo()
        return True
    else:
        return False

def Fjogador1(jogador):
    Flinha()
    resp = int(input("{}, em qual posição você gostaria de marcar? ".format(jogador)))
    Flinha()

    #Verifica se o número digitado está entre as posições possíveis
    while resp < 1 or resp > 9:
        resp = int(input("{}, somente posições entre 1 a 9. ".format(jogador)))
        cls()
        Ftabuleiro()

    #Marca "X" na posição digitada caso a mesma esteja vazia
    if resp in range(1,10):
        if resp == 1 and tabuleiro[0][0] == 1:
            tabuleiro[0][0] = "X"
        elif resp == 2 and tabuleiro[0][1] == 2:
            tabuleiro[0][1] = "X"
        elif resp == 3 and tabuleiro[0][2] == 3:
            tabuleiro[0][2] = "X"
        elif resp == 4 and tabuleiro[1][0] == 4:
            tabuleiro[1][0] = "X"
        elif resp == 5 and tabuleiro[1][1] == 5:
            tabuleiro[1][1] = "X"
        elif resp == 6 and tabuleiro[1][2] == 6:
            tabuleiro[1][2] = "X"
        elif resp == 7 and tabuleiro[2][0] == 7:
            tabuleiro[2][0] = "X"
        elif resp == 8 and tabuleiro[2][1] == 8:
            tabuleiro[2][1] = "X"
        elif resp == 9 and tabuleiro[2][2] == 9:
            tabuleiro[2][2] = "X"
        else:
            Fposicao(jogador)
            cls()
            Ftabuleiro()
            Fjogador1(jogador)
    cls()
    Ftabuleiro()
    Flinha()
    return "X"

def Fjogador2(jogador):
    Flinha()
    resp = int(input("{}, em qual posição você gostaria de marcar? ".format(jogador)))
    Flinha()

    #Verifica se o número digitado está entre as posições possíveis
    while resp < 1 or resp > 9:
        resp = int(input("{}, somente posições entre 1 a 9. ".format(jogador)))
        cls()
        Ftabuleiro()
    #Marca "O" na posição digitada caso a mesma esteja vazia
    if resp in range(1,10):
        if resp == 1 and tabuleiro[0][0] == 1:
            tabuleiro[0][0] = "O"
        elif resp == 2 and tabuleiro[0][1] == 2:
            tabuleiro[0][1] = "O"
        elif resp == 3 and tabuleiro[0][2] == 3:
            tabuleiro[0][2] = "O"
        elif resp == 4 and tabuleiro[1][0] == 4:
            tabuleiro[1][0] = "O"
        elif resp == 5 and tabuleiro[1][1] == 5:
            tabuleiro[1][1] = "O"
        elif resp == 6 and tabuleiro[1][2] == 6:
            tabuleiro[1][2] = "O"
        elif resp == 7 and tabuleiro[2][0] == 7:
            tabuleiro[2][0] = "O"
        elif resp == 8 and tabuleiro[2][1] == 8:
            tabuleiro[2][1] = "O"
        elif resp == 9 and tabuleiro[2][2] == 9:
            tabuleiro[2][2] = "O"
        else:
            Fposicao(jogador)
            cls()
            Ftabuleiro()
            Fjogador2(jogador)
    cls()
    Ftabuleiro()
    Flinha()
    return "O"


#DEFINIÇÕES
tabuleiro = [[1,2,3],[4,5,6],[7,8,0]]
cond = "sim"
import os
#CÓDIGO
while cond != "nao":
    resp = -1
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    while resp != 0:
        print("Bem vindo ao Jogo da Velha.")
        print("Vamos começar?\n")

        jogador1 = input('JOGADOR 01, Digite seu nome: ')
        jogador2 = input('JOGADOR 02, Digite seu nome: ')
        Ftabuleiro()
        cont = 0
        for c in range(5):
            j1 = Fjogador1(jogador1)
            cont += 1
            if Fchecar(j1) is True:
                resp = 0
                print('{} GANHOU!!!!'.format(jogador1))
                Flinha()
                break
            if Fempate(cont) is True:
                print('Empate!!!!!')
                Flinha()
                break
            j2 = Fjogador2(jogador2)
            cont += 1
            if Fchecar(j2) is True:
                resp = 0
                print('{} GANHOU!!!!'.format(jogador2))
                Flinha()
                break
            if Fempate(cont) is True:
                print('Empate!!!!!')
                break
        resp = 0
    cond = input('Quer jogar novamente? Digite "sim" ou "nao": ')
