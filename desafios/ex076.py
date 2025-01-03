produtos = ('Carro', 250000, 'Casa', 500000,
            'Rolex', 30000, 'Celular', 4000)
print('Produtos e preços:')
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]} --------- ', end='')
    else:
        print(f'R$ {produtos[c]:.2f}')
