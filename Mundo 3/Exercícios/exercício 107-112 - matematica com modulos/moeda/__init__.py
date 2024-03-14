def metade(n,monetario=False):
    n/=2
    if monetario:
        rs='R$'+str(n)
    return rs

def dobro(n,monetario=False):
    n*=2
    if monetario:
        rs='R$'+str(n)
    return rs

def aumento(n,a,monetario=False):
    n+=n*a/100
    if monetario:
        rs='R$'+str(n)
    return rs

def redução(n,d,monetario=False):
    n-=n*d/100
    if monetario:
        rs='R$'+str(n)
    return rs

def monetario(n):
    rs='R$'+str(n)
    return rs

def resumo(n,a,d):
    print(f'''
{"="*30}
{"Resumo do Valor":^30}
{"="*30}''')
    print(f'{"Preço analisado:":<20}{"R$":>2} {n:.2f}')
    print(f'{"Dobro do preço:":<20}{"R$":>2} {n*2:.2f}')
    print(f'{"Metade do preço:":<20}{"R$":>2} {n/2:.2f}')
    print(f'{a}{"% de aumento:":<18}{"R$":>2} {n+(n*a/100):.2f}')
    print(f'{d}{"% de redução:":<18}{"R$":>2} {n-(n*d/100):.2f}')