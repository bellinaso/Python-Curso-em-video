teste='   Só Testando Esse Comando Mesmo  '
print(teste)
n1=(teste.strip())
print (n1.count('e',4,35))
print (n1.find('Testando'))
print ('Testando' in n1)
print (n1.replace('Comando','sé loco tio'))
print (n1.capitalize())
print (len(n1))
n2=(n1.split()) #separa a string
print(n2[1])
# (teste.upper/lower() deixa maiusculo ou minusculo)
print(teste.title()) #igual captalize porém em todas palavras
# r/l+strip() (e outros comandos) server para indicar lado esquerdo ou direito
# '-'.join(teste) junta as strings com o caractere dentro da string no comando
# para atribuir comandos se deve criar uma variavel com os mesmos
#print=(n2[0])
