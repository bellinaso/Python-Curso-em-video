from datetime import date
data=date.today().year
maior=0
menor=0
for n1 in range(1,8):
    n1=int(input('{}Em que ano a {}ª pessoa nasceu: '.format('\033[32m')))
    idade=data-n1
    if idade>=21:
        maior+=1
    else:
        menor+=1
print('Ao todo são {} pessoas de maior.')
print('E no total são {} de menor.')
# vi a resolução
