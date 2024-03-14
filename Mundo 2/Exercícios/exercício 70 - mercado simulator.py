total=milhares=menor=0
maisbarato=''
print('='*33)
print('   Gerenciador de mercadorias')
print('='*33)
while True:
    n1=str(input('Digite o nome do produto: '))
    n2=float(input('Digite o preço do produto: '))
    print('='*33)
    total+=n2 # total gasto
    if n2>999: # quantos valem mais de 1000
        milhares+=1
    if menor==0 or n2<menor:
        menor=n2
        maisbarato=n1
    opção=str(input('Você deseja registrar mais um produto? [s/n] '))
    if opção in 'Nn':
        break
print('='*33)
print(f'''O total gasto em compras foi de: R${total:.2f}
A quantidade de produtos que valem mais de R$1000,00 é de: {milhares}
O produto mais barato foi {maisbarato} e custou R${menor:.2f}''')
