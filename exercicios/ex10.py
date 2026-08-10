# 6 — Soma dos elementos com try-except

numeros = [10, 20, 30, 40, 50]

try:
    soma = 0

    for numero in numeros:
        soma += numero

    print(f"A soma é: {soma}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")