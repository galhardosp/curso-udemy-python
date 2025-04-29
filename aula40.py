while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador desejado: ')

    numeros_validos = None

    try:
        float_1 = float(numero_1)
        float_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos')
            

        operadores_permitidos = '+-/*'

        if operador not in operadores_permitidos:
            print('O operador é inválido')

        # if len(operador) > 1:
        #     print('Digite apenas um operadr')
        # continue
        ###

        print('Realizando sua cobnta confira o resulrtado abaixo')

        if operador == '+':
            print(float_1 + float_2)
        elif operador == '-':
            ...
        elif operador == '/':
            ...
        elif operador == '*':
            ...


    sair = input('Deseja sair ? [S]im ').lower().startswith('s')

    if sair is True:
        break
    
        
