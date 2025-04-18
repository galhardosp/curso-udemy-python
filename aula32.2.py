nome = input('Escreva seu nome: ')

nome_len = len(nome)

if nome_len <= 4:
    print('Seu nome é curto')
elif nome_len >= 5 and nome_len < 6:
    print('Seu nome é normal')
elif nome_len > 6:
    print('Seu nome é muito grande')