from sys import stdout
from os import write
from time import sleep
login=''
senha=''
senha2='********'
menu=''
print('Starting C:/users/user/documents/Aniversário.py')
sleep(0.1)
print('Aguarde...')
sleep(1.5)
print('==='*10)
while login != 'Luca':
    login=str(input('{}Digite seu endereço de login: '.format('\033[37m')).lower().capitalize())
    if login != 'Luca':
        print('{}Login inválido :/ \nTente novamente.'.format('\033[31m'))
        print('{}Dica: nome do aniversariante.'.format('\033[32m'))
print('==='*10)
while senha != '09032010':
    senha=str(input('{}Digite sua senha: '.format('\033[37m')).lower())
    if senha != '09032010':
        print('Carregando...')
        sleep(0.5)
        print('{}Senha incorreta. \nTente novamente.'.format('\033[31m'))
        print('{}Dica: data do aniversariante.'.format('\033[32m'))
sleep(0.3)
for i in senha2:
    stdout.write(i)
    stdout.flush()
    sleep(0.1)
print('{}\nLogin completo'.format('\033[32m'))
print('{}==='.format('\033[37m')*10)
print('''{}     Menu     
[1] Aniversário
[2] Jogos
[3] Configurações
[4] Sair'''.format('\033[32m'))
while menu != '1' and menu != 'aniversário' and menu != '4' and menu != 'sair':
    menu=str(input('{}Escolha aqui: '.format('\033[32m')).lower())
    if menu != '1' and menu != 'aniversário' and menu != '4' and menu != 'sair':
        print('{}Operação inválida.'.format('\033[31m'))
if menu=='1' or menu=='aniversário':
    msg=('{}Luca nosso primo, hoje é teu dia! E por isso eu, Bruno, Gabriel e Gabriela, estamos te enviando esta mensagem para desejar feliz aniversário! Que tu possa ter muitos anos de vida e seja sempre feliz.\n{}Novamente grande abraço e tudo de bom pra ti hoje!'.format('\033[36m','\033[34m'))
for i in msg:
    stdout.write(i)
    stdout.flush()
    sleep(0.01)
n1=input('')
