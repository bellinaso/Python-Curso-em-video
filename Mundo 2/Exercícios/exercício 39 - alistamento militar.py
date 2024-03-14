#import datetime
#date = datetime.date.today()
#print(f"Current Year -> {date.year}")

from datetime import date
print('{}Você será avaliado para o alistamento militar.'.format('\033[31m'))

data=date.today()
ano=data.year #atual

n1=int(input('Em que ano você nasceu?{} '.format('\033[32m')))
idade=ano-n1
if idade>18:
    resto=idade-18
    print('Você deveria ter se alistado há {} anos.\nSe apresente no quartel urgente.'.format(resto))
elif idade<18:
    resto=18-idade
    print('Você ainda tem tempo para se alistar. Faltam {} anos.'.format(resto))
