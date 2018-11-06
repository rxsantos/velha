# Exercício Final - AV em Grupo
##
##  RAFAEL MACHADO PEREIRA .
##  ROBERTO XAVIER DOS SANTOS .
##  TATIANE TONET LUGLI .

# JOGO DA VELHA

# FUNÇÕES

def Ftabuleiro():  # Exibe o tabuleiro atual
    print("A seguir, o tabuleiro atualizado.\n")
    for i in range(3):
        print(tabuleiro[i])


def Fempate():  # Verifica se houve empate
    print('Empate!!!!!')
    Flinha()
    cond = input('Vocês querem jogar novamente? Digite "sim" ou "nao": ')
    while cond != 'sim' and cond != 'nao':
        cond = input('Por favor, digite somente "sim" ou "nao": ')
    return cond


def Freinicar(jogador):  # Verifica se os jogadores querem jogar novamente
    cond = input('{}, quer jogar novamente? Digite "sim" ou "nao": '.format(jogador))
    while cond != 'sim' and cond != 'nao':
        cond = input('{}, por favor, digite somente "sim" ou "nao": '.format(jogador))
    return cond


def Flinha():  # Exibe uma linha
    print("=-" * 32)


def Ffimjogo(jogador):  # Exibe mensagem de Fim de Jogo
    print("************************FIM DE JOGO*****************************")
    print('{} GANHOU!!!!'.format(jogador))


def Fquantpar(par, cont1, cont2, jogador1, jogador2):
    emp = par - (cont1 + cont2)

    print('Quantidade de partidas jogadas: {}'.format(par))
    print('Quantidade de empates: {}'.format(emp))
    print('Quantidade de partidas vencidas por {}: {}'.format(jogador1, cont1))
    print('Quantidade de partidas vencidas por {}: {}'.format(jogador2, cont2))
    if cont1 == cont2:
        print('Os jogadores permaneceram empatados!!!!')
    elif cont1 > cont2:
        print('O jogador que ganhou mais partidas foi o {}, com {} partida(s) ganha(s).'.format(jogador1, cont1))
    else:
        print('O jogador que ganhou mais partidas foi o {}, com {} partidas ganha(s).'.format(jogador2, cont2))


def Fposicao(jogador):  # Exige mensagem de Posição Utilizada
    print("{}, esta posição já foi utlizada, por favor digite outra posição.".format(jogador))


def Fchecar(x, jogador):  # Faz a checagem de vencedor.
    # diagonal principal
    if tabuleiro[0][0] == x and tabuleiro[1][1] == x and tabuleiro[2][2] == x:
        Ffimjogo(jogador)
        return True
    # diagonal secundária
    elif tabuleiro[0][2] == x and tabuleiro[1][1] == x and tabuleiro[2][0] == x:
        Ffimjogo(jogador)
        return True
    # linha 01
    elif tabuleiro[0][0] == x and tabuleiro[0][1] == x and tabuleiro[0][2] == x:
        Ffimjogo(jogador)
        return True
    # linha 02
    elif tabuleiro[1][0] == x and tabuleiro[1][1] == x and tabuleiro[1][2] == x:
        Ffimjogo(jogador)
        return True
    # linha 03
    elif tabuleiro[2][0] == x and tabuleiro[2][1] == x and tabuleiro[2][2] == x:
        Ffimjogo(jogador)
        return True
    # coluna 01
    elif tabuleiro[0][0] == x and tabuleiro[1][0] == x and tabuleiro[2][0] == x:
        Ffimjogo(jogador)
        return True
    # coluna 02
    elif tabuleiro[0][1] == x and tabuleiro[1][1] == x and tabuleiro[2][1] == x:
        Ffimjogo(jogador)
        return True
    # coluna 03
    elif tabuleiro[0][2] == x and tabuleiro[1][2] == x and tabuleiro[2][2] == x:
        Ffimjogo(jogador)
        return True
    else:
        return False


def Fjogador1(jogador):
    Flinha()
    resp = int(input("{}, em qual posição você gostaria de marcar? ".format(jogador)))
    Flinha()

    # Verifica se o número digitado está entre as posições possíveis
    while resp < 1 or resp > 9:
        resp = int(input("{}, somente posições entre 1 a 9. ".format(jogador)))
        Ftabuleiro()

    # Marca "1" na posição digitada caso a mesma esteja vazia
    if resp in range(1, 10):
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
    Flinha()
    resp = int(input("{}, em qual posição você gostaria de marcar? ".format(jogador)))
    Flinha()

    # Verifica se o número digitado está entre as posições possíveis
    while resp < 1 or resp > 9:
        resp = int(input("{}, somente posições entre 1 a 9. ".format(jogador)))
        Ftabuleiro()
    # Marca "2" na posição digitada caso a mesma esteja vazia
    if resp in range(1, 10):
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


# DEFINIÇÕES
cond = "sim"
contj1 = 0
contj2 = 0
contpar = 0
# CÓDIGO
print("Bem vindo ao Jogo da Velha.")
print("Vamos começar?\n")
jogador1 = input('JOGADOR 01, digite seu nome: ')
jogador2 = input('JOGADOR 02, digite seu nome: ')

while cond != "nao":
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    resp = -1
    contpar += 1
    while resp != 0:
        print("A seguir, o mapa de posições do tabuleiro.\n")
        print("[ 1 2 3 ]")
        print("[ 4 5 6 ]")
        print("[ 7 8 9 ]")
        Ftabuleiro()
        cont = 0

        for c in range(5):
            j1 = Fjogador1(jogador1)
            cont += 1
            if Fchecar(j1, jogador1) is True:
                resp = 0
                Flinha()
                contj1 += 1
                cond = Freinicar(jogador1)
                if cond == "nao":
                    Fquantpar(contpar, contj1, contj2, jogador1, jogador2)

                break
            if cont == 9:
                if Fempate() == "nao":
                    Fquantpar(contpar, contj1, contj2, jogador1, jogador2)
                    cond = 'nao'
                    break
                else:
                    cond = 'sim'
                break
            j2 = Fjogador2(jogador2)
            cont += 1
            if Fchecar(j2, jogador2) is True:
                resp = 0
                Flinha()
                contj2 += 1
                cond = Freinicar(jogador2)
                if cond == "nao":
                    Fquantpar(contpar, contj1, contj2, jogador1, jogador2)

                break
            if cont == 9:
                if Fempate() == "nao":
                    Fquantpar(contpar, contj1, contj2, jogador1, jogador2)
                    cond = 'nao'
                    break
                else:
                    cond = 'sim'
                break
        resp = 0
