# Fazer um Pojeto de Palpites, que o usuario vai tenta adivinhar o mesmo numero que o computador escolheu
# onde o usuário vai colocar um numero inteiro. se o usuário colocar alguma letra, o
# programa deve escrever uma mensagem de erro que só aceita numeros e pedi para o usuário escolher o numero novamente.
# Obs: colocar cores no Programa e coloca os acertos que o Usuário teve.

from jogo_palpites.funcionalidades import *

titulo('Jogo de Palpites')
tenteadivinha('Tente Adivinha qual Número estou pensando entre 1 e 10')
p = palpite('\033[0:35:40mDigite um Palpite:\033[m ')
# Projeto Resolvido
