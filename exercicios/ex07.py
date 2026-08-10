# 3 — Soma dos números ímpares de 1 a 10

soma = 0

for numero in range(1, 11):
    if numero % 2 != 0:
        soma += numero

print(f"A soma dos números ímpares é: {soma}")