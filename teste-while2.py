import random
# numero_sorteado = '9'
# numero_sorteado_float = float(9)
# sorteio = '0'
# sorteio_float = float(sorteio)
# resultado_float = True

# while resultado_float != numero_sorteado_float:
#     resultado = input('Escolha um número de 1 á 10: ')
#     resultado_float = float(resultado)
#     if resultado_float == numero_sorteado:
#         print('Parabéns, vc acertou')
#     else:
#         print('Tente novamente')

# numero_secreto = random.randint(1, 10)
pergunta = ''
numero_secreto = random.randint(1, 10)
pergunta_int = ''

while pergunta_int != numero_secreto:
    pergunta = input('Digite um número: ')
    pergunta_int = int(pergunta)
    if pergunta_int != numero_secreto:
        print('Tente novamente')

print('Parabens')