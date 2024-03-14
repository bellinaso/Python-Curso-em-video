print('{}Informe a seguir as informações necessárias para calcular o seu {}IMC'.format('\033[33m','\033[4;32m'))
n1=float(input('Digite seu peso: '))
n2=float(input('Digite sua altura em metros: '))
imc=n1/(n2**2)
print('{}==='.format('\033[0;35m')*10)
if imc<=18.5:
    print('{}Seu IMC é {:.2f} . Você está abaixo do peso. Cuide-se.'.format('\033[31m',imc))
elif imc>18.5 and imc<=25:
    print('{}Seu IMC é {:.2f} . Você está no peso normal.'.format('\033[32m',imc))
elif imc>25 and imc<=30:
    print('{}Seu IMC é {:.2f} . Você possui sobrepeso, se cuide.'.format('\033[33m',imc))
elif imc>30 and imc<=35:
    print('{}Seu IMC é {:.2f} ! Você possui obesidade, se cuide!'.format('\033[33m',imc))
elif imc>35:
    print('{}Seu IMC é {:.2f} !!! Você possui obesidade mórbida! Procure um médico.'.format('\033[31m',imc))
