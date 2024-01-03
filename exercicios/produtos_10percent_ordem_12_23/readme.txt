Exercício
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

Código:
Este código realiza as seguintes operações:

1. Importa as bibliotecas necessárias (`copy` para cópia profunda) e o módulo `produtos` do pacote `dados`.
2. Aumenta o preço de cada produto em 10% e cria uma lista chamada `novos_produtos` contendo os produtos originais com os preços alterados.
3. Define uma função chamada `exibir` que imprime os elementos de uma lista.
4. Cria duas cópias profundas da lista `novos_produtos` chamadas `produtos_ordenados_por_nome` e `produtos_ordenados_por_preco`.
5. Ordena `produtos_ordenados_por_nome` em ordem decrescente com base no nome dos produtos.
6. Ordena `produtos_ordenados_por_preco` em ordem crescente com base no preço dos produtos.
7. Exibe os seguintes resultados:
   - Lista original de produtos.
   - Lista de novos produtos com preços aumentados.
   - Lista de produtos ordenados por nome de forma decrescente.
   - Lista de produtos ordenados por preço de forma crescente.

Código criado em Dezembro de 2023