nome = input("Digite seu nome: ")
N = nome.upper()
n = nome.lower()
c = len(nome.replace(" ", ""))
p = len(nome.split()[0])
print("Nome: {}.\nNome: {}.\nQuantidade de letras: {} letras.\n"
      "Quantidade de Letras Primeiro Nome: {} letras".format(N, n, c, p))