"""
Exercício: Calculadora de IMC (Índice de Massa Corporal)

Crie um programa que calcule o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos pelo usuário. 
O IMC é calculado usando a seguinte fórmula:

IMC = peso (kg) / (altura (m) * altura (m))

O programa deve realizar as seguintes etapas:

Peça ao usuário para inserir seu peso em quilogramas.
Peça ao usuário para inserir sua altura em metros.
Calcule o IMC com base nas entradas do usuário.
Exiba o valor do IMC e a seguinte classificação:
IMC menor que 18,5: Abaixo do peso
IMC entre 18,5 e 24,9: Peso normal
IMC entre 25,0 e 29,9: Sobrepeso
IMC entre 30,0 e 34,9: Obesidade Grau I
IMC entre 35,0 e 39,9: Obesidade Grau II
IMC maior ou igual a 40,0: Obesidade Grau III (Mórbida)
Dica: Use uma estrutura condicional (if/elif/else) para determinar a classificação do IMC com base no valor calculado.

Veja se consegue implementar esse programa. 
Quando terminar, você pode compartilhar sua solução e, se desejar, posso fornecer feedback ou mostrar a solução completa.
"""

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