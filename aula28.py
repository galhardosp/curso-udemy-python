nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome:
    print(nome) #printa o nome
    print(nome[::-1]) #printa o nome ao contrário
if ' ' in nome: #verifica sem há espaços no nome
    print('Seu nome contém espaços')
else:
    print('Seu nome não contém espaços')
if nome:     
    print("Seu nome tem ", (len(nome)), "letras") #printa a quantidade de letras no seu nome
    print(nome[0]) #printa a primeira let ra
    print(nome[-1]) #printa a ultima letra
else:
    print('Desculpa, vc deixou campos vazios')
