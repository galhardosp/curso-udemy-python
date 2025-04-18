#interpolação de string com %

# s - SyntaxWarning

# d e i - int

# f - float

# x e x - hexadecimal(ABCDEF0123456)     

nome = 'jeffao'
preco = 10000.123456

variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)