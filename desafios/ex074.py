import random
sorteado = [random.randint(0, 100) for c in range(5)] # Vai sortear 5 números de 0 a 100
print(f'Os valores sorteados foram: {sorteado}')
print(f'O menor número é {min(sorteado)}')
print(f'O maior número é {max(sorteado)}')