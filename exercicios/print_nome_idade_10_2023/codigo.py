from datetime import datetime, timedelta

nome = input('Olá, por favor, digite seu nome: ')
idade = input('Digite sua idade: ')
data_atual = datetime.today().year
idade_2052 = (2052-data_atual)+int(idade)

if nome.replace(" ", "").isalpha() and idade.isdigit():
    print(
        f'Seu nome é "{nome.capitalize()}", e sua idade é "{idade}".\n' 
        f'Seu nome invertido é "{nome[::-1]}".'
    )
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
    
    print(
        f'Seu nome contém {len(nome)} caracteres.\n'
        f'A primeira letra do seu nome é: {nome[0]}.\n' 
        f'A última letra do seu nome é: {nome[-1]}.\n'
        f'Em 2052 você terá {idade_2052} anos' 
    )
else:
    print('Desculpe, insira em "Nome" apenas letras e em "Idade" apenas numeros')