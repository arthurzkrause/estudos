#Função para colocar texto na formatação "...",

texto = """
Esta é a primeira linha.
Esta é a segunda linha.
Esta é a terceira linha.
"""

def colocar_entre_aspas(texto):
  linhas = texto.splitlines()
  texto_modificado = ""
  for linha in linhas:
    texto_modificado += f'"{linha}",\n'

  return texto_modificado

texto_modificado = colocar_entre_aspas(texto)

print(texto_modificado)