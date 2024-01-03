import random
from perguntas import cem_perguntas

def perguntas_random():
    quantidade = 0

    while quantidade != 3:
        primeira_pergunta = random.choice(cem_perguntas)
        print(primeira_pergunta)
        quantidade += 1

perguntas_random()