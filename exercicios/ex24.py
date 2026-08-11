# Aprovando empréstimo

salario = int(input("Digite sua renda mensal: "))
valor_parcela = int(input("Digite o valor da parcela desejada: "))

if valor_parcela > (salario * 0.3):
    print("Empréstimo negado! O valor da parcela excede 30% da sua renda.")
else:
    print("Empréstimo aprovado! O valor da parcela está dentro do limite permitido.")