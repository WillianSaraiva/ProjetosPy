# Criando um dicionario com alguns pares chave-valor
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "Sao Paulo"
}

# Acessando e imprimindo valores individuais usando chaves
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cidade: {cidade}')

# Adicionando um novo par chave-valor ao dicionario
dicionario["profissao"] = "Engenheira"
print(f'Dicionario apos adicionar profissao: {dicionario}')

# Modificando o valor associado a uma chave existente
dicionario["idade"] = 26
print(f'Dicionario apos modificar a idade: {dicionario}')

# Removendo um par char-valor do dicionario
del dicionario["cidade"]
print(f'Dicionario apos remover a cidade: {dicionario}')

# Acessando todas as chaves e valores do dicionario
chaves = dicionario.keys()
valores = dicionario.values()

print(f'Chaves: {list(chaves)}')
print(f'Valores: {list(valores)}')

# Iterando sobre os pares chave-valor do dicionario
print('Iterando sobre o dicionario:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

# Verificando se uma chave existe no dicionario
if"nome" in dicionario:
    print(f'O nome no dicionario e: {dicionario["nome"]}')
else:
    print('A chave "nome" nao esta no dicionario')

# Usando o metodo ge() para acessar valores de forma segura
profissao = dicionario.get("profissao", "Desconhecido")
print(f'Profissao: {profissao}')

# Limpando todos os elementos do dicionario
dicionario.clear()
print(f'Dicionario apos limpar todos os elementos: {dicionario}')
