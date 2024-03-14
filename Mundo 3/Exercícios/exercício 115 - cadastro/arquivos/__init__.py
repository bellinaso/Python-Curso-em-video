from sistem import cabeçalhoMenu
from utility import cores

def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close
    except:
        print('\033[31mHouve um erro na Criação do arquivo \033[m')
    else:
        print('Arquivo criado com sucesso.')

def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('\033[31mErro ao ler o arquivo \033[m')
    else:
        cabeçalhoMenu('CADASTROS')
        print(cores(5),end='')
        print(a.read())
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido',idade=0):
    try:
        a=open(arquivo,'at+')
    except:
        print('Houve um erro na leitura do arquivo.')
    else:
        try:
            a.write(f'Nome: {nome:<35}  Idade: {idade} \n')
        except:
            print('Houve um erro na tentativa de escrever os dados!')
        else:
            print(f'Novo registro de {nome}')