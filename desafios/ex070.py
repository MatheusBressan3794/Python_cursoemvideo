resposta = 's'
gasto = produtos = cont = 0

while resposta == 's':
    cont += 1
    nome = input('Nome do produto: ')
    preço =float(input('Qual o preço do produto em R$: '))
    gasto += preço

    if preço >= 1000:
        produtos += 1
    if cont == 1:
        barato1 = nome
        barato2 = preço
    elif barato2 > preço:
        barato1 = nome
        barato2 = preço

    resposta = input('Deseja continuar? [s/n] ')

print(f'Você gastou {gasto:.2f}R$')
print(f'{produtos} custaram mais de 1000R$')
print(f'O produto mais barato foi: {barato1}, que custou {barato2:.2f}R$')