nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Nota: {media:.2f} - Aprovado")
elif media >= 5:
    print(f"Nota: {media:.2f} - Recuperação")
else:
    print(f"Nota: {media:.2f} - Reprovado")