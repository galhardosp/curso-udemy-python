"""
While dentro de while

"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'Linhas: {linha}, colunas: {coluna}')
        coluna = coluna + 1

    linha = linha + 1

print('Acabou')
