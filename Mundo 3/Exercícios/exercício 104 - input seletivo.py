def linha():
    print('='*50)


def leia(num):
    while True:
        linha()
        n=str(input(num))
        if n.isnumeric():
            int(n)
            linha()
            return n
            break
        else:
            linha()
            print(f'"{n}" NÃO é um número válido. Por favor tente novamente.')

n=leia('Digite um número: ')
print(f'Você digitou o número {n}')