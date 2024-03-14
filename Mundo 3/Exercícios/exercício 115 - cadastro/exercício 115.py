import utility
import sistem
import arquivos
from time import sleep

arquivo='cadastros.txt'
if not arquivos.arquivoExiste(arquivo):
    arquivos.criarArquivo('cadastros.txt')

while True:
    sistem.cabeçalhoMenu('MENU PRINCIPAL')
    sistem.textoMenu()
    opção=sistem.menu('{}Opção: {}'.format(utility.cores(3),utility.cores(4)))  

    if opção==1:
        arquivos.lerArquivo('cadastros.txt')

    elif opção==2:
        
        nome=str(input('Digite o nome: ').strip().title())
        idade=sistem.leiaInt('Digite a idade: ')
        arquivos.cadastrar('cadastros.txt',nome,idade)


    elif opção==3:
        print(utility.cores(5),end='')
        utility.linha(52)
        print('Finalizando sistema, até logo!')
        sleep(1)
        break