from random import randint
from time import sleep
print('{}Aguarde a roleta{}'.format('\033[31m',format('\033[32m')))
for i in range(3,0,-1):
    print(i)
    sleep(0.5)
print('{}O valor escolhido foi {}{}'.format('\033[37m','\033[32m',randint(0,8)))
