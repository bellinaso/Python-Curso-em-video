def escreva(texto):
    tamanho=len(texto)
    linha='='*tamanho
    print(linha)
    print(texto)
    print(linha)

msg=(str(input('Digite uma palavra ou frase: ')))
escreva(msg)