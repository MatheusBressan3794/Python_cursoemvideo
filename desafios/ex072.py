tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        pergunta = int(input('Digite um númeroentre 0 e 20: '))
        if pergunta > 20 or pergunta < 0:
            print('Esse número não está entre 0 e 20. ')
        else:
            break
    print(f'Você digitou o número {tupla[pergunta]}')
    continuar = input('Deseja continuar? (s/n) ')
    if continuar == 'n':
        break
print('Obrigado por usar o programa')