idadecont=0
sexo=opção=''
sexom=sexof=0
print('='*20)
print('   Cadastro')
print('='*20)
while True:
    while True:
        n1=str(input('Digite o sexo: '))[0]
        if n1 in 'MmFf':
            break
        else:
            print('Sexo inválido. Tente novamente')
    print('='*20)
    n2=int(input('Digite a idade: '))
    print('='*20)
    opção=str(input('Você deseja escrever mais informações? [s/n] '))
    if n2>18:
        idadecont+=1
    if n1 in 'Mm':
        sexom+=1
    if n1 in 'Ff' and n2<20:
        sexof+=1
    if opção in 'Nn':
        break
print(f'Foram registradas {idadecont} pessoas com mais de 18 anos, {sexom} homens, e {sexof} mulheres com menos de 20 anos.')
