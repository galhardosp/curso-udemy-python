#try e except introdução

# numero_str = input(
#     'vou dobrar oq vc digitar: '    
# )

#print(numero_str.isdigit()) #esse is digit no final é booleando, se for não forem numeros inteiros ele responde como false, se for. true

numero_str = input(
    'vou dobrar oq vc digitar: '    
)

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')
