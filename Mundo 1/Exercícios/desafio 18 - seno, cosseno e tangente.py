import math
an=float(input('Escreva um ángulo cujo deseja calcular o Seno, cosseno e sua tangente: '))
se=math.sin(math.radians(an))
co=math.cos(math.radians(an))
tg=math.tan(math.radians(an))
print('O seno vale {:.2f} \nO cosseno vale {:.2f} \nE a tangente vale {:.2f}'.format(se, co, tg))
