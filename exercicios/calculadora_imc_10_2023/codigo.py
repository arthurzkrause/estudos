import os

while True: #optou-se pelo uso de while para que o usuário chegue ao fim do programa, sem necessidade de reiniciá-lo caso digitar algo errado.
    print("Bem-vindo à calculadora de IMC")
    peso = input("Por favor, insira o seu peso em quilos: ")
    altura = input("Por favor, insira a sua altura em metros: ")

    # Substituir vírgulas por pontos, se existirem. Caso usuário utilize ".", será deleta na próxima etapa.
    peso = peso.replace(",", ".")
    altura = altura.replace(",", ".")

    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura * altura)

        if 0.00 <= imc < 0.01:
            print (f"Você digitou {altura} centímeros, por favor, digite em metros. Exemplo: {(altura/100):.2f}.")
        elif imc < 18.5:
            print(f"Seu IMC é {imc:.2f}: Você está abaixo do peso.")
        elif 18.5 <= imc < 25:
            print(f"Seu IMC é {imc:.2f}: Você está com peso normal.")
        elif 25 <= imc < 30:
            print(f"Seu IMC é {imc:.2f}: Você está com sobrepeso.")
        elif 30 <= imc < 35:
            print(f"Seu IMC é {imc:.2f}: Você está com Obesidade Grau I.")
        elif 35 <= imc < 40:
            print(f"Seu IMC é {imc:.2f}: Você está com Obesidade Grau II.")
        else:
            print(f"Seu IMC é {imc:.2f}: Você está com Obesidade Grau III")

        break
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('Por favor, digite um número válido.')
        print()