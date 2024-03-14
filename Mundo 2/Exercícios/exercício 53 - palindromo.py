n1=str(input('Digite uma frase: ')).strip().lower()
lista=n1.split() # separa a string em palavras
frase=''.join(lista) # junta a lista com o que tem dentro da string
invert=frase[::-1] # pega do início ao fim da frase e inverte
#invert='' #nada
#for i in range(len(frase)-1,-1,-1): # conta de trás pra frente a string
#    invert+=frase[i] # nova variavel que cria uma frase com o inverso
print('O inverso de "{}" é "{}"'.format(n1,invert))
if invert==frase:
    print('Essa frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo.')
# assisti a resolução
