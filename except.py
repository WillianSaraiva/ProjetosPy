def calcular_expressao():
    expressao = input("Digite uma expressao matematica:")     # Solicitar ao usuario que insira uma expressao matematica

    try:
        resultado = eval(expressao)     # Avaliar a expressao usando eval
        print("O resultado da expressao e:", resultado)
    except Exception as e:
        print("Erro ao avalidar a expressao:", e)

calcular_expressao() #Chama a funcao
#Exemplo da chamada do programa:
#Digite uma expressaomatematica: 2 + 3 * (4 - 1)
#O resultado da expressao e: 11
