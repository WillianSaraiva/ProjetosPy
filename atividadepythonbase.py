valor1 = int(input("Digite um numero inteiro:"))
valor2 = float(input("Digite um numero de ponto flutuante"))
valor3 = input("Digite um valor booleano (True ou False):").lower() == "true"

print("Numero inteiro:", valor1, type(valor1))
print("Numero de ponto flutuante:", valor2, type(valor2))
print("Valor booleano:", valor3, type(valor3))