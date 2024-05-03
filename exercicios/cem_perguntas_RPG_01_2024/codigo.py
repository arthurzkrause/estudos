import random
from perguntas import cem_perguntas

def perguntas_random(quantos):
    quantidade = 0

    while quantidade != quantos:
        primeira_pergunta = random.choice(cem_perguntas)
        print(f'- {primeira_pergunta}')
        quantidade += 1
while True:
    quantos = input('Quantas perguntas você quer?')
    if quantos.isdigit():
        quantos = int(quantos)
        break
    else:
        print('Digite apenas números')

perguntas_random(quantos)