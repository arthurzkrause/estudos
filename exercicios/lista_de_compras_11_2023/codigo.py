import os

lista_completa = []

while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir, [a]pagar, [l]istar, [c]oncluir: ").lower()

    if opcao == "i":
        os.system('cls')
        objeto = input("Digite o que deseja adicionar: ")
        lista_completa.append(objeto)
        print(f"{objeto} foi adicionado à lista.")

    elif opcao == "a":
        os.system('cls')    
        objeto = input("Digite o que deseja apagar: ")
        if objeto in lista_completa:
            lista_completa.remove(objeto)
            print(f"{objeto} foi apagado da sua lista.")
        else:
            print(f"{objeto} não está em sua lista.")

    elif opcao == "l":
        os.system('cls')
        if len(lista_completa) == 0:
            print('Nada para listar')
        for indice, nome in enumerate(lista_completa): #"for" não faz nada em lista vazia
            print(indice, nome)

    elif opcao == "c":
        break

    else:
        os.system('cls')
        print("Opção inválida. Por favor, escolha uma opção válida (i, a, l, c).")