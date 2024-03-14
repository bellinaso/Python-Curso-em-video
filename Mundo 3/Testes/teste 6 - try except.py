while True:
    try:
        n1=int(input('Digite um numerador: '))
        n2=int(input('Digite outro denominador: '))
        resp=n1/n2
    except ValueError:
        print('Encontramos o problema "Value Error"! O valor indicado não corresponde com o sistema.')
    except ZeroDivisionError:
        print('Encontramos o problema "Division by zero"! Zero não pode dividir ou ser dividído.')
    except Exception as erro:
        print(erro.__class__)
    else:
        print(f'O resultado é {resp}')
        break
'''finally:
    print('Volte sempre!')'''