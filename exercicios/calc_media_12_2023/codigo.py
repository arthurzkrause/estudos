lista_numeros =[
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [0,0,0,0,0,0,0,0,0,0],
    [],
]

def calcula_media(media):
    quantidade_itens = len(media)
    total = 0

    if quantidade_itens == 0:
        return 0

    for numeros in media:
        total += numeros

    media_total = total / quantidade_itens
    return media_total


for lista in lista_numeros:
    if lista == []:
        print(f"lista vazia, portanto, média {calcula_media(lista)}")
    else:
        print(
            f'O números {lista} possuem média: {calcula_media(lista):.2f}.'
        )