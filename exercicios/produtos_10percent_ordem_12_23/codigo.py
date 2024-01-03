import copy
from dados.produtos import produtos

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1,2)}
    for produto in copy.deepcopy(produtos)
]

def exibir(produtos):
    for item in produtos:
        print(item)
    print()

#Nome decrescente
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)

#Preço crescente
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])

print("Produtos originais:")
exibir(produtos)

print("Novos produtos com preços aumentados em 10%:")
exibir(novos_produtos)

print("Produtos ordenados por nome decrescente:")
exibir(produtos_ordenados_por_nome)

print("Produtos ordenados por preço crescente:")
exibir(produtos_ordenados_por_preco)