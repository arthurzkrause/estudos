TAREFA: 
Calculadora de IMC (Índice de Massa Corporal)

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


Este código em implementa uma calculadora de Índice de Massa Corporal (IMC).

Entra em um loop infinito, permitindo que o usuário corrija as entradas se necessário, sem precisar reiniciar o programa.
Solicita ao usuário que insira o peso e a altura.
Substitui vírgulas por pontos nas entradas, se existirem.
Tenta converter as entradas para números de ponto flutuante.
Calcula o IMC usando a fórmula: IMC = peso / (altura * altura).
Exibe uma mensagem com base no valor do IMC:
    IMC abaixo de 18.5: "Você está abaixo do peso."
    IMC entre 18.5 e 25: "Você está com peso normal."
    IMC entre 25 e 30: "Você está com sobrepeso."
    IMC entre 30 e 35: "Você está com Obesidade Grau I."
    IMC entre 35 e 40: "Você está com Obesidade Grau II."
    IMC acima de 40: "Você está com Obesidade Grau III."
Se a altura inserida for próxima de 0, o programa informa ao usuário que a altura deve ser inserida em metros.
Se ocorrer uma exceção durante a conversão (por exemplo, se o usuário inserir texto em vez de números), 
o programa exibe uma mensagem de erro, limpa a tela e solicita uma nova entrada.
O loop continua até que o usuário forneça entradas válidas e o cálculo do IMC seja concluído com sucesso.

Texto revisado.
Gerado por https://chat.openai.com/

Código criado em Outubro de 2023