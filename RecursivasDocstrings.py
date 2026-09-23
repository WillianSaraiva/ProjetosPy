#Funcao recursiva ccontagem regressiva

def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print('acabou')
regressiva(10)

#Nao recursiva
for y in range(10, -1, -1):
    print(y)
print('acabou')