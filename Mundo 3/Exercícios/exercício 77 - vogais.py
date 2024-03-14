words='amor','sagaz','mexer','exceto','gentil','mundo','safado','computador','teclado','dicionario'
for i in words:
    print(f'\nNa palavra {i.upper()} temos: ',end='')
    for letras in i:
        if letras in 'aeiou': # as palavras da tupla são uma lista
            print(letras,end=' ')
# assisti a resolução