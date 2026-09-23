def conta_test():
    nr = int(input('Digite  um numero: '))
    s = nr * 3
    print(s)
    q = 12 / s
    print(q)

while True:
    try:
        conta_test()
        break
    except ValueError:
        print('Entre com um numero valido')
    except ZeroDivisionError:
        print('O numero nao pode ser zero')