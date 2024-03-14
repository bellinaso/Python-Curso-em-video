def fatorial(num,show=False):
    """
    :param num: O numero que será calculado o fatorial.
    :param show: Decide por True or False se será mostrado o passo a passo dos fatores.
    :return: Retorna o valor do fator."""
    fator=1
    for n in range(num, 0, -1):
        if show:
            print(n,end='')
            if n>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        fator*=n
    return fator


n1=int(input('Digite um número para o caluclo da fatorial: '))
show=str(input('Você deseja mostrar o cálculo? [s/n] '))
if show=='s':
    show=True
else:
    show=False
print(fatorial(n1,show))
print(help(fatorial))