for raiz in range(32, 100):
    num = raiz * raiz #Calcula o numero gerado pela raiz
    menor = num % 100 #Obtem o numero dos algarismos menos significativos
    maior = num // 100 #Obtem o numero dos algarismos mais significativos

    if(menor + maior) == raiz: #Valida se a raiz corresponde a soma
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu', raiz)