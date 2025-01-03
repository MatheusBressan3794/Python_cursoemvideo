palavras = ('aprender', 'programar', 'python', 'linguagem', 'curso', 'grátis','estudar', 'praticar', 'trabalhar', 'mercado', 'programar', 'futuro')
for p in palavras:# Cada palavra da tupla
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:# Cada letra da palavra 
        if letra.lower() in 'aáàãâeéèêiíìîoóòõôuúû':# Se tiver a,e,i,o,u na palavra ele vai mostrar
            print(letra, end=' ')