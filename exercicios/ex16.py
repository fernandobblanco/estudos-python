print ("Monitorando vendas no comércio")

produto1 = int(input("Digite as vendas do Produto 1: "))
produto2 = int(input("Digite as vendas do Produto 2: "))

if produto1 > produto2:
    print("Produto 1 teve mais vendas!")
elif produto2 > produto1:
    print("Produto 2 teve mais vendas!")
else:
    print("Os produtos tiveram o mesmo número de vendas!")
    
