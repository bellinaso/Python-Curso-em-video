n1=counter=0
tabuada=1
print('''
.-----.     .-.                   .-.         .-..-..----.
`-. .-'     : :                   : :         : :: :`--  ;
  : : .--.  : `-. .-..-. .--.   .-' : .--.    : :: : .' ' 
  : :' .; ; ' .; :: :; :' .; ; ' .; :' .; ;   : `' ; _`,`.
  :_;`.__,_;`.__.'`.__.'`.__,_;`.__.'`.__,_;   `.,' `.__.' ''')
while True:
    counter=0
    tabuada=1
    print('(Números negativos param o programa)\n')
    n1=int(input('Digite um número: '))
    if n1<0:
        break
    while True:
        if counter<10:
            counter+=1
            tabuada=n1*counter
            print(f'{n1}x{counter}={tabuada}')
        else:
            break
print('fim')
