import random, os


def jogo_de_adivinhacao(max_tentativas=10):
    numero_secreto = random.randint(1, 50)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número, você consegue adivinha qual é?")

    while tentativas < max_tentativas:
        palpite = input("Faça seu palpite: ")
        
        try: palpite = int(palpite)
        except:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Digite um número válido.")
            continue
        
        tentativas += 1

        if palpite < numero_secreto:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Tente um número mais alto.")
        elif palpite > numero_secreto:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Tente um número mais baixo.")
        else:
            os.system('clear' if os.name == 'posix' else 'cls')
            if tentativas >= 15:
                print(f'Caraca, ia tentar todos os números? {tentativas} tentativas! Ainda bem que acabou')
            else:
                print(f"Parabéns! Você conseguiu! Levou só {tentativas} tentativas.")
            break

    if tentativas == max_tentativas:
        print(f"Você atingiu o número máximo de tentativas. O número secreto era {numero_secreto}.")

jogo_de_adivinhacao(max_tentativas=10)