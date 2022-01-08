from random import randint
from time import sleep


def palpite(n):
    """
    -> Funcionamento dos palpites
    :param n: numero que o usuario Digito
    :return: Não tem
    - > Função Criar Pelo Matheus
    """
    computador = randint(1, 10)
    cont = 0
    while True:
        try:
            usuario = int(input(n))
        except (ValueError, TypeError):
            print('\033[0:31:40mErro! Teve um Problema com os tipos de dados que voce digitou\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0:33:40mO Usuário Preferiu Não Digitar nada\033[m')
            break
        else:
            if usuario == 999:
                print('\033[1:37mPrograma Encerrado !\033[m')
                print(f'\033[36mO Usuário teve {cont} Acertos\033[m')
                break
            elif usuario > 10 or usuario < 1:
                print('\033[31mDigite um Número só entre 1 e 10 Por Favor !\033[m')
            if usuario == computador:
                print(f'\033[0:34:40mComputador Escolheu: {computador} e o Usuário Escolheu: {usuario}\033[m')
                print('\033[0:34:40mParabéns Você Acertou o Mesmo Número que o Computador !\033[m')
                computador = randint(1, 10)
                cont += 1
            elif usuario != computador:
                print(f'\033[0:34:40mComputador escolheu um Número Diferente\033[m')
                if usuario < computador:
                    print('\033[0:34:40mDigite um Valor Maior\033[m')
                elif usuario > computador:
                    print('\033[0:34:40mDigite um Valor Menor\033[m')


def titulo(msg):
    """
    -> Vai fazer um Titulo
    :param msg: Mensagem do Titulo do Jogo
    :return: Não tem
    -> Função Criada Pelo Matheus
    """
    print('\033[32m-\033[m' * 40)
    print(f'\033[32m{msg}\033[m'.center(48))
    print('\033[32m-\033[m' * 40)


def tenteadivinha(msg):
    """
    -> vai mostrar o que o Usuário tem que fazer para encerrar o programa e dizer para o usuario para tenta
    adivinha qual número o computador está pensando
    :param msg: vai escrever uma mensagem na tela, para o Usuário tenta adivinha o Número que o Computador está
    pensando
    :return: Não tem
    -> Função Criada Pelo Matheus
    """
    print('\033[33mDigiete 999 para Encerrar o Programa\033[m')
    print(f'\033[7::40m{msg}\033[7::40m', end='')
    print('\033[7::40m.\033[m', end='')
    sleep(0.7)
    print('\033[7::40m.\033[m', end='')
    sleep(0.7)
    print('\033[7::40m.\033[m')
    sleep(0.7)

