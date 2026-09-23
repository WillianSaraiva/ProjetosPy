vnr = eval(input("Digite um numero:"))
print("Valor digitado", vnr)
print("antes do if")
if vnr <= 100:
    print("Entrou no if do 100")
elif vnr <= 500:    #NAO E IDENTADO
    print("Entrou no elif do 500")
elif vnr <= 1000:  # NAO E IDENTADO
    print("Entrou no elif do 1000")
else:
    print("Entrou no else")

print("Saiu do if")