while True:
    try:
        nr = int(input('Digite um numero: '))
        s = nr * 3
        print(s)
        q = 12 / s
        print(q)
    except ValueError:
        print('Entre com um numero valido')
    except ZeroDivisionError:
        print('O numero nao pode ser zero')
    else:
        print('Entrou no else')
        break
    finally:
        print('Entrou no fanally')