# 7 — Média com tratamento de lista vazia

numeros = [10, 20, 30, 40, 50]

try:
    media = sum(numeros) / len(numeros)
    print(f"A média é: {media}")

except ZeroDivisionError:
    print("Não é possível calcular a média de uma lista vazia.")