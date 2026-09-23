for num in range(1000, 10000):
    menor = num % 100 # Obtem o numero dos algarismos menos significativos
    maior = num // 100 # Obtem o numero dos algarismos mais significativos
    raiz = menor + maior # Obtem a raiz

    if (raiz * raiz) == num: # Valida se a taiz gera o numero testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu', num)