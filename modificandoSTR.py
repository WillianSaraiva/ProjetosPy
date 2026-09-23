# Criando uma string
texto = "Ola, Mundo"

# Acessando caracteres individuais
primeiro_caractere = texto[0]
ultimo_caractere = texto[-1]

print(f'Primeiro caractere: {primeiro_caractere}')
print(f'Ultimo caractere: {ultimo_caractere}')

# Fatiando uma string
sub_texto = texto[5:10]
print(f'Substring (indices 5 a 9): {sub_texto}')

# Concatenando strings
saudacao = "Ola"
nome = "Alice"
frase = saudacao +", " + nome + "!"
print(f' Frase concatenada: {frase}')

# Dividindo uma string em uma lista
lista_palavras = texto.split()
print(f'Lista de palavras: {lista_palavras}')

# Substituindo partes de uma string
texto_modificado = texto.replace("Mundo", "pyhthon")
print(f' Texto modificado: {texto_modificado}')

# Convertendo para maiusculas e minusculas
texto_maiusculo = texto.upper()
texto_minuscula = texto.lower()
print(f'Texto em maiusculas: {texto_maiusculo}')
print(f'Texto em minusculas: {texto_minuscula}')

# Removendo espacos em branco (trin
texto_espacos = "    Ola, Mundo!    "
texto_sem_espacos = texto_espacos.strip()
print(f'Texto sem espacos extras: {texto_sem_espacos}')

# Verificando a presenca de substring
if "Mundo" in texto:
    print('A palavras "Muindo" esta presente no texto.')

# Formatacao de strings
idade = 30
cidade = "Sao Paulo"
frase_formatada = f'Meu nome e {nome}, tenho {idade} anos e moro em {cidade}'
print(f'Frase formatada: {frase_formatada}')

# Outro metodo de formatacao
frase_formatada_2 = "Meu nome e {}, tenho {} anos e moro em {}.".formate(nome, idade, cidade)
print(f'Outra frase formatada: {frase_formatada_2}')
