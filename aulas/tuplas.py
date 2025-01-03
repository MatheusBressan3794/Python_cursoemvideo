lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
print(lanche)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Ou')
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')