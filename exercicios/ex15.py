# contar a frequência de cada palavra em uma frase

frase = """
Python é uma linguagem de programação muito popular.
Python é fácil de aprender e Python é muito utilizado.
Muitas pessoas estudam Python porque Python possui uma sintaxe simples.
Empresas também utilizam Python para desenvolvimento, dados e automação.
"""
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)