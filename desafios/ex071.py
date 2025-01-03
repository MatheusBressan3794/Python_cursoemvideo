print('Bem-vindo ao caixa eletronico')
quantidade = int(
    input('Qual a quantidade de dinheiro você deseja sacar? (Número intero): '))
total = quantidade
ced = 50
notas = 0
while True:
    if total >= ced:  # Se o valor for maior que o valor de cédula
        total -= ced  # Subtrai o valor da cédula
        notas += 1  # Quantidade de notas
    else:  # Se não, diminui o valor da cédula e repete até zerar o valor
        if notas > 0:  # Só vai escrever se a quantidade de cédulas for mair que 0
            print(f'{notas} notas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        notas = 0
        if total == 0:
            break
