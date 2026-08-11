#Temperatura dos servidores

temperatura = int(input("Digite a temperatura atual: "))

if temperatura < 0:
    print("Temperatura muito baixa! Risco de congelamento.")
elif temperatura <= 25:
    print("Temperatura ideal para os servidores.")
else:
    print("Temperatura alta! Risco de superaquecimento.")