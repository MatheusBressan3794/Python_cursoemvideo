tupla = (int(input('Digite um número: ')),
 int(input('Mais um: ')),
 int(input('Próximo: ')),
 int(input('Outro: ')),
 int(input('Último: ')))
print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')# Conta quantas vezes apareceu o 9
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}º posição')# Posição do 3
else:
    print('O valor três não foi digitado')
print('Os valores pares são:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')