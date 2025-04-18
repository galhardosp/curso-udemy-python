entrada = input('[E]ntrar [S]air: ')
senha = input('senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrou')
else:
    print('Saiu')