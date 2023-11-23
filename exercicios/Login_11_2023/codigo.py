#Coleta de informações
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email(email):
    caracter_email = '@'
    return caracter_email in email

def criar_conta():
    print('Bem-vindo à página de login.\n'
          'Vamos criar sua conta.')

    while True:
        usuario_1['email'] = input('Por favor, insira seu e-mail: ')
        if validar_email(usuario_1['email']):
            limpar_tela()
            print('E-mail, já foi!\n')
        else:
            limpar_tela()
            print("Por favor, digite um e-mail que contenha '@'")
            continue

        usuario_1['senha_digitada'] = input('Agora, insira sua senha: ')
        usuario_1['senha_repetida'] = input('Repete pra nós confirmarmos ela: ')
        if usuario_1['senha_digitada'] == usuario_1['senha_repetida']:
            limpar_tela()
            print('Suas senhas conferem.')
            break
        else:
            limpar_tela()
            print("Senhas diferentes. Por favor, insira novamente suas informações.")
            continue

usuario_1 = {}
criar_conta()

#Login
while True:
    print("Selecione uma opção:")
    opcao = input("[L]ogin ou [S]air.").lower()

    if opcao == "l":
        limpar_tela()
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        if email == usuario_1['email'] and senha == usuario_1['senha_digitada']:
            print("Bem-vindo ao sistema")
            break
        else:
            print("Seus dados não conferem, tente novamente")
            continue
    elif opcao == "s":
        limpar_tela()
        print("Você optou por sair. Até breve!")
        break 
    else:
        limpar_tela()
        print("Opção inválida. Por favor, escolha uma opção válida (L ou S).")