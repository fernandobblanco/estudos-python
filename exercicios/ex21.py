entrada = int(input("Digite a hora atual (formato 24h): "))

if entrada < 8 or entrada > 18:
    print("Fora do horário de expediente.")
else:
    print("Dentro do horário de expediente.")