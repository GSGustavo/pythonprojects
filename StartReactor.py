from random import randint
from os import system
from time import sleep

# Variáveis do sistema
posicoes_sorteadas = list()  # Aqui serão guardados todas as posições sorteadas pelo programa
barra_de_progresso = list()  # Lista para guardar os valores da barra de progresso
errou = False  # Variável feita para verificar o acerto do usuário
# Variáveis do sistema

pos = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
#        1       2       3       4       5       6       7       8        9
# Variável feita para comparar a entrada do usuário com a posição da matriz do programa
# Ja que é mais pratico digitar a posição absoluta do que a posição técnica ex: 1,0


# Funções do programa
class Cores:
    erro = '\033[31m'
    fim = '\033[0m'


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Separador simples
def sep():
    print('=-' * 20, end='=')
    print()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Titulo
def titulo(value):
    sep()
    print(f'{value:^40}')
    sep()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Erros
def erro():
    print(f'{Cores.erro}ERRO: Valor Inválido!{Cores.fim}')


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Erro customizado, ou seja, o programador passa a mensagem de erro que vai aparecer
def erro_customizado(value):
    print(f'{Cores.erro}{value}{Cores.fim}')


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Quero que esse programa tenha a menor taxa de erro possível
# E para isso fiz essa função que verifica a entrada do usuário e não deixa-o passar até que a entrada seja um inteiro
def verificar_int(questao):
    while True:
        try:
            verificar = int(input(questao))
            break
        except ValueError:
            erro()
    return verificar


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Função especifica para verificar a saída de algo
def verificar_saida(questao):
    while True:
        try:
            verificar = str(input(questao)).upper()
            if verificar in 'SN':
                break
            else:
                erro()
        except ValueError:
            erro()
    return verificar
# Função especifica para verificar a saída de algo
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Funções do programa


# Programa Principal
while True:  # while para ver se o jogador vai continuar jogando ou não
    posicoes_sorteadas.clear()
    # Nivel: Normal
    system('cls')
    titulo('Start Reactor - Among Us')
    print('''Bem-Vindo(a) ao jogo!
Menu de Níveis:
[1] = Normal / Contém 4 rodadas, possui auxílio e é um pouco devagar;
[2] = Médio / Contém 7 Rodadas, possui auxílio e é um pouco rápido;
[3] = Difícil / Contém 10 Rodadas, não possui auxílio e é rápido!''')
    while True:  # while para verificar se o nível está entre 1 e 3
        lvl = verificar_int('Qual nível quer escolher? ')
        if 1 <= lvl <= 3:
            break
        erro()

    # Verificando qual o nível escolhido pelo usuário e escolhendo o número de rodadas
    if lvl == 1:
        lvl = 4
    elif lvl == 2:
        lvl = 7
    else:
        lvl = 10
    # Verificando qual o nível escolhido pelo usuário e escolhendo o número de rodadas

    # Sorteando posições aleatórias
    for sorteado in range(0, lvl):
        random = [randint(0, 2), randint(0, 2)]
        posicoes_sorteadas.append(random[:])
    # Sorteando posições aleatórias

    # Mostrando a matriz para o usuário ver e decorar
    for d in range(1, lvl + 1):  # for para repetir as jogadas de acordo com o nível
        # Printando a Matriz
        for j in range(0, d + 1):  # for para repetir as jogadas até chegar no lvl
            system('cls')
            titulo('Start Reactor - Among Us')

            # Limpando a barra de progresso para não acumular strings
            barra_de_progresso.clear()
            # Limpando a barra de progresso para não acumular strings

            # Verificando a rodada pro progress bar não dar bug
            for etapa in range(0, lvl):
                barra_de_progresso.append('▢')
            if j != d:
                ad = 1
            else:
                ad = 0
            for etapa in range(0, j + ad):
                barra_de_progresso[etapa] = '■'
            # Verificando a rodada pra barra de progresso não dar bug

            print(f'{"Barra de Progresso":^40}')
            print(*barra_de_progresso)
            print()

            # Auxílio
            if lvl in [4, 7]:
                ajuda = 1
            else:
                ajuda = '▪'
            # Auxílio

            # Mostrando a matriz de fato
            for linha in range(0, 3):  # for para printar a matriz
                for coluna in range(0, 3):  # for para printar a matriz

                    # Escondendo a matriz para não ajudar o jogador
                    if j != d:
                        if linha == posicoes_sorteadas[j][0] and coluna == posicoes_sorteadas[j][1]:
                            print(f"{f'{ajuda}  █  ▪':^13}", end='')
                        else:
                            print(f"{f'{ajuda} ███ ▪':^13}", end='')
                    else:
                        print(f"{f'{ajuda} ███ ▪':^13}", end='')
                    # Escondendo a matriz para não ajudar o jogador

                    if lvl in [4, 7]:
                        ajuda += 1
                print()
                print()
                print()
            # Printando a Matriz

            # Definindo o tempo de acordo com o level
            if lvl == 4:
                sleep(1.5)
            elif lvl == 7:
                sleep(1)
            else:
                sleep(0.5)
            # Definindo o tempo de acordo com o level

        sep()
        errou = False

        # Perguntando a posição para o usuário e verificando a mesma
        for pergunta in range(0, d):
            while True:
                perguntar = verificar_int('Qual a posição do botão? ')
                if 1 <= perguntar <= 9:
                    break
                erro()
            if perguntar != pos.index(posicoes_sorteadas[pergunta]) + 1:
                errou = True
                break
        # Perguntando a posição para o usuário e verificando a mesma

        # Verificando se o usuário errou a posição, se sim, quebramos o programa
        if errou:
            erro_customizado('Você errou a posição, boa sorte na próxima!')
            break
        # Verificando se o usuário errou a posição, se sim, quebramos o programa
    # Mostrando a matriz para o usuário ver e decorar

    # Verificando se o jogador errou ou não, caso não, damos o parabéns para ele
    if not errou:
        print('Parabéns você completou o jogo, sua memória é boa!')
    sep()
    # Verificando se o jogador errou ou não, caso não, damos o parabéns para ele

    # Verificando Saída
    while True:
        sair = verificar_saida('Quer continuar jogando? [S: Sim / N: Não] ')
        if sair != "":
            break
        erro()
    if sair == 'N':
        break
    # Verificando Saída

    system('cls')
