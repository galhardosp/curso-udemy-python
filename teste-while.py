soma = 0
contagem = 0

while soma <= 100:
    numero = input('Digite um número ')
    int_numero = int(numero)
    soma = int_numero + int_numero
    contagem += 1
    if soma > 100:
        print(f'foram digitados {contagem} números')
