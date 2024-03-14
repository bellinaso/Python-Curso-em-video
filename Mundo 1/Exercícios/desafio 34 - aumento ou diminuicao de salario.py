n1=float(input('Digite seu salário: R$'))
if n1<=1250:
    n2=n1+(n1*10/100)
    print('Você ganhou um aumento de 10%! Agora seu salário é: R${:.2f}'.format(n2))
if n1>=1250:
    n3=n1-(n1*15/100)
    print('Seu salário está muito alto e foi reajustado para -15% :( Agora ele é: R${}'.format(n3))
