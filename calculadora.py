while True:
    print('===Cauculadora===')
    print('''
    Escolha uma opção:
    1-soma
    2-subtrair
    3-multiplicar
    4-dividir
    5-porcentagem
    x-Sair   
    ''')

    opcao = input('Escolha uma opção:')

    if opcao == 'x':
        print('Encerrando...')
        break

    if opcao in ('1', '2', '3', '4'):
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))

    if opcao == '3':

        print('O resultado é:',n1 * n2)
