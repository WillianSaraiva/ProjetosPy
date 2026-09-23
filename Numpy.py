#Utilizando o numpy para calcular as raizes
#Importando o numpy
import numpy as np

#Funcao para calcular as raizes da equacao de segundo grau
def calcular_raizes(a, b, c):
    #Coeficientes da equacao
    coeficientes = [a, b, c]

    #Usando numpy.roots para calcular as raizes
    raizes = np.roots(coeficientes)
    return raizes
#Solicitando os coeficientes ao usuario
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

#Calculando as raizes
raizes = calcular_raizes(a, b, c)

#Imprimindo os resultados
print(f"As raizes da equacao sao: {raizes[0]} e {raizes[1]}")
