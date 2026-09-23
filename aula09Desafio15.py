dias = int(input("Quantos dias alugados: "))
km = float(input("Quantos km rodados: "))
real = float(dias * 60) + float(km * 0.15)
print("A quantidade total de R${:.2f}".format(real))