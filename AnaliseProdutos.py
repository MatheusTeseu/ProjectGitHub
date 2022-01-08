# Crie um Programa que analise qual é o Número Mario e qual é o numero menor e quantos itens foram digitados. e dizer a
# media entre todos os itens e qual foi a forma de pagamento escolhido pelo usuario e se tem desconto ou juros na compra
# e o total da compra, O Programa deve aceitar um comando para encerrar o programa,
# caso não tiver mais nada para adicionar, ex: 999
# Forma de pagamento:
# Dinheiro a Vista  10 % de Desconto
# Cartão de Débito a Vista 7 % de Desconto
# Cartão de Crédito a Vista 5% de Desconto
# Cartão de Crédito  mais de 1x 15 % de Juros

total = maior = menor = cont = media = valor_produto = pagamento = 0
nome = ''
while True:
    nome_produto = str(input('Digite o Nome do Produto: ')).title().strip()
    preco_produto = float(input('Digite o Valor do Produto: '))

    print('Parcelamento só Aceita no Cartão de Crédito !')
    print('[ 1 ] Dinheiro\n[ 2 ] Cartão de Débito\n[ 3 ] Cartão de Crédito')
    opcao = ' '
    while opcao not in '123':
        opcao = str(input('Digite a Opção desejavel de acordo com as Opções acima: '))
    vezes = int(input('Quantas Vezes ? '))
    if opcao == 1 and vezes == 1:
        pagamento = preco_produto - (preco_produto * 10 // 100)
        total += pagamento

    elif opcao == 2 and vezes == 1:
        pagamento = preco_produto - (preco_produto * 7 // 100)
        total += pagamento
        cont += 1
    elif opcao == 3 and vezes == 1:
        pagamento = preco_produto - (preco_produto * 5 // 100)
        total += pagamento
        cont += 1
    elif opcao == 3 and vezes > 1:
        pagamento = preco_produto + (preco_produto * 15 // 100)
        total += pagamento
        cont += 1
    """if cont == 1:
        maior = pagamento
        menor = pagamento
        nome = nome_produto
    elif pagamento > maior:
        maior = pagamento
        nome = nome_produto
    elif pagamento < menor:
        menor = pagamento
        nome = nome_produto"""
    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Tem Algo mais para Adicionar [S/N] ? ')).capitalize()[0].strip()
    if adicionar == 'N':
        break

print(f'O Total do Pagamento foi: {total}\nO Preço Maior foi {nome} que Custo: R${maior:.2f}')
print(f'O Preço Menor foi {nome} que Custo: R${menor:.2f}')
