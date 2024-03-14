def monetario(msg):
    while True:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[31m> Erro! "{entrada}" é um parâmetro inválido.\033[m')
        else:
            return float(entrada)
            break