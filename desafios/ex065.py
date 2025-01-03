contador = 0
ultimo = 1
soma = media = maior = menor = 0
pergunta = 's'
print('Digite 0 para saber a média')
while pergunta == 's':
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    pergunta = input('Deseja continuar? [s/n] ')
    if pergunta == 'n':
        contador += -1
        media = soma / contador
        print(f'A média dos números digitados foi {media:.2f}')
        print(f'O maior número digitado foi {maior}')
        print(f'O menor número digitado foi {menor}')
        resposta = input('Deseja continuar?(s/n) ').upper()