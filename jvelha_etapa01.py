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

#DEFINIÇÕES
tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]
#cond = "sim"

#CÓDIGO

print("Bem vindo ao Jogo da Velha.")
print("Vamos começar?\n")

jogador1 = input('JOGADOR 01, Digite seu nome: ')
jogador2 = input('JOGADOR 02, Digite seu nome: ')


Ftabuleiro()
