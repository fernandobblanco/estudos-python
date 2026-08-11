km = int(input("Digite a distância em km: "))

if km <= 100:
    print("Preço da corrida: R$ 10,00")
elif km <= 200:
    print("Preço da corrida: R$ 20,00")
else:
    print("Preço da corrida: R$ 30,00")