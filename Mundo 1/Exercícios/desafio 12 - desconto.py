n1=float(input('Digite o preço do produto: '))
pc=n1*5/100
desc=n1-pc
print('O preço do produto com desconto de 5% é: R${:.2f}'.format(desc))
