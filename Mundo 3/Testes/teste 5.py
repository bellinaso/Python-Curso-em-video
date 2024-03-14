def linha(teste):
    '''
    > Esta função cria uma linha com 30 caracteres, um texto, e mais uma linha'''
    print('='*30)
    print(teste)
    print('='*30)


def soma(*val): # função de soma misturada com linha
    '''
    > Esta função somará os valores definidos'''
    somas=0
    for num in val:
        somas+=num
    return somas

def contador(*num):
    tamanho=len(num)
    print(f'Recebi os valores {num} e são {tamanho} números.')


def dobra(*numeros):
    for i in numeros:
        i*=2
        #print(i,end=' ')
    return i


linha('bandeirantes')

print(soma(1, 1, 4, 6)) # utilizado o comando return

contador(6,4,6,8,3)

r1=dobra(0,2,3,5,6)
print(r1)


# dentro de uma função, o comando "global" cria um laço entre o escopo (variavel) local e o escopo global.