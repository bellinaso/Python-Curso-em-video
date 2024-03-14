with open("codigo.txt","at+") as arq:
    arq.write("n=int(input('Entre com um numero'))\n")
    for i in range(2**32):
        if i%2==0:
            arq.write(f"""
if n=={i}:print('par')\n""")
        else:
            arq.write(f"""
if n=={i}:print('impar')\n""")