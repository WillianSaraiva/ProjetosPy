p = float(input("Digite o preco do produto: R$ "))
d = (5 * p) / 100
print("O valor do produto originalmente e R$ {:.2f} com desconto 5% fica R$ {:.2f}".format(p, (p-d)))
