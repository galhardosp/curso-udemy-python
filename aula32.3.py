numero = input('Informe um número: ')

try:
    numero_int = int(numero)
    conta = numero_int % 2
    if conta == 0:
        print('Seu numero é par')
    elif conta:
        print('Seu número é impar')
except ValueError:
    print('Não é um número inteiro')
