from datetime import date
data=date.today()
ano_atual=data.year
correct=False
info={
    'nome':'',
    'nascimento':0,
    'idade':0
}
info['nome']=str(input('Digite seu nome: ').title().strip())
info['nascimento']=int(input('Digite seu ano de nascimento: '))
info['idade']=ano_atual-info['nascimento']
if info['idade']>=14:
    info['ctps']=int(input('Digite o número da sua carteira de trabalho: (0 caso não tenha) '))
    if info['ctps']>0:
        while not correct:
            info['contratação']=int(input('Digite o ano de contratação: (0 para não contratado) '))
            if info['contratação']==0:
                break
            if info['contratação']>=(info['nascimento']+14):
                info['salário']=float(input('Digite o valor do seu salário: R$ '))
                info['tempo trabalhando']=ano_atual-info['contratação']
                info['aposentadoria']=((info['contratação']+35)-info['tempo trabalhando'])
                correct=True
print('='*30)
for i in info:
    print(f'{i.capitalize()}: {info[i]}')
# falta calcular:

# quanto tempo está trabalhndo
# como calcular:
# ano de contratação - ano atual

# ano de aposentadoria (em base 35 anos)
# como calcular:
# ((ano de contratação + 35) - tempo trabalhando) - ano atual