#formatação de numeros

a = 'A'
b = 'B'
c = 1.1111

# formato = 'a={} b={} c={:2f}'.format(a, b, c)

formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)

print(formato)