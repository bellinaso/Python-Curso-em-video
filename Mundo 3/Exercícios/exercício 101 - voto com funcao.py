from datetime import date
data=date.today()
ano_atual=data.year

def voto(nascimento):
    idade=ano_atual-nascimento
    if idade<16:
        print(f'Com {idade} anos, o voto NÃO é permitido.')
    elif idade<18 and idade>=16 or idade>=70:
        print(f'Com {idade} anos, o voto é OPCIONAL.')
    else:
        print(f'Com {idade} anos, o voto é OBRIGATÓRIO.')


while True:
    ano_nascimento=int(input('Digite o ano que você nasceu: '))
    if ano_nascimento>ano_atual:
        print('Você não pode escolher um ano inválido!')
    else:
        voto(ano_nascimento)
        break
