perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Função para apresentar uma pergunta e receber a resposta do usuário
def fazer_pergunta(pergunta):
    print(pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções'], 1):
        print(f"{i}) {opcao}")

    while True:
        resposta_usuario = input("Digite a opção correta: ")
        try:
            resposta_usuario = int(resposta_usuario)
            if 1 <= resposta_usuario <= len(pergunta['Opções']):
                break
            else:
                print("Digite um número válido dentro do intervalo das opções.")
        except ValueError:
            print("Digite um número válido.")

    return resposta_usuario

# Função para verificar se a resposta está correta
def verificar_resposta(pergunta, resposta_usuario):
    return pergunta['Opções'][int(resposta_usuario) - 1] == pergunta['Resposta']

# Função principal
def main():
    pontuacao = 0

    for pergunta in perguntas:
        resposta_usuario = fazer_pergunta(pergunta)
        if verificar_resposta(pergunta, resposta_usuario):
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta era: {pergunta['Resposta']}\n")

    print(f"Sua pontuação final é: {pontuacao}/{len(perguntas)}")

# Executar o programa
if __name__ == "__main__":
    main()