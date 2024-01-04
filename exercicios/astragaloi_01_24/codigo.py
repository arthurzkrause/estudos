import random
from astragaloi_texto import texto_oracular

def perguntas_random():
    quantidade = 0
    leituras = int(input("Quantas leituras você gostaria de fazer?"))

    while quantidade != leituras:
        primeira_pergunta = random.choice(texto_oracular)
        print(f'{primeira_pergunta}\n')
        quantidade += 1

perguntas_random()