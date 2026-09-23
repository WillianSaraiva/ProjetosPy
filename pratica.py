hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

quantidade_hamburguer = int(input("Digite a quantidade de hamburguer:"))
quantidade_batata = int(input("Digite a quantidade de batata:"))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerante:"))

preco_total = float((hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante))

print(f"Seu pedido e: Hamburguer: {quantidade_hamburguer} und, Batata Frita: {quantidade_batata} und, Refrigerante: {quantidade_refrigerante} und.")
print(f"Valor que devera ser pago: R${preco_total: .2f}")
