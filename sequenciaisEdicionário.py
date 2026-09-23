# Criando uma lista com alguns elementos
lista = [10, 20, 30, 40, 50]

# Acessando elementos individuais da lista
primeiro_elemento = lista[0]
segundo_elemento = lista[1]

# Imprimindo os elementos acessados
print(f'O primeiro elemento da lista e {primeiro_elemento}')
print(f'O segundo elemento da lista e {segundo_elemento}')

# Adicionando um elemento ao final da lista
lista.append(60)
print(f'Lista apos adicionar 60: {lista}')

# Inserindo um elemento em uma posicao especifica
lista.insert(2, 25) #Insjerindo 25 na posicao 2
print(f'Lista apos inserir 25 na posicao 2: {lista}')

# Removendo um elemento da lista
lista.remove(40) # Remove o primeiro valor 40 encontrado
print(f'Lista apos remover 40: {lista}')

# Removendo o ultimom elemento da lista
ultimo_elemento = lista.pop()
print(f'Elemento removido: {ultimo_elemento}')
print(f'Lista apos remover o ultimo elemento: {lista}')

# Acessando um subngrupo da lista (fatiamento)
sub_lista = lista[1:4]
print(f'Sub-lista (elementos de indice 1 a 3): {sub_lista}')

# Ordenando a lista
lista.sort()
print(f'Lista ordenada: {lista}')

# Iterando sobre os elementos da lista
print('Iterando sobre a lista:')
for elemento in lista:
    print(elemento)
