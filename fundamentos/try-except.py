try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou: {numero}")

except ValueError:
    print("Você precisa digitar um número válido.")