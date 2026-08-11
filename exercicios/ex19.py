# Calculando o IMC

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

IMC = peso / (altura **2)

if IMC < 18.5:
    print("Abaixo do peso")
    print("IMC:", IMC)
elif 18.5 <= IMC < 25:
    print("Peso normal")
    print("IMC:", IMC)
else:
    print("Acima do peso")
    print("IMC:", IMC)