# Calculando o tempo total de projeto

A = int(input("Informe os dias para a atividade A: "))
B = int(input("Informe os dias para a atividade B: "))
C = int(input("Informe os dias para a atividade C: "))

if A < 0 or B <0 or C < 0:
    print("Erro: O número de dias não pode ser negativo.")
else:
    tempo_total = A + B + C
    print("O tempo total do projeto é de", tempo_total, "dias.")
