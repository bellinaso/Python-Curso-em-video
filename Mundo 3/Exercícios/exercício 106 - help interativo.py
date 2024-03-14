while True:
    print('{}Sistema de ajuda PyHelp'.format('\033[37m'))
    print('(Digite "Fim" para finalizar)')
    command=str(input('Função: '))
    if command.strip().lower()=='fim':
        break
    print('{}'.format('\033[32m'))
    print(help(command))
