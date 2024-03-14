import moeda
import dados

num=dados.monetario('Digite o valor: R$')

print('='*60)

print(f'A metade de {moeda.monetario(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.monetario(num)} é {moeda.dobro(num,True)}')
print(f'Aumento de 10% de {moeda.monetario(num)} dão {moeda.aumento(num,10,True)}')
print(f'Redução de 13% de {moeda.monetario(num)} dão {moeda.redução(num,13,True)}')

print('='*60)

moeda.resumo(num,80,35)