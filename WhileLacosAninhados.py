while True:
    print("Voce esta no primeiro laco.")
    opcao1 = input("Deseja sair dele? Digite SIM para isso.\n")
    if opcao1 == "SIM":
        break   # este break é do primeiro laço
    else:
        while True:
            print("Voce esta no segundo laco.")
            opcao2 = input("Deseja sair dele? Digite SIM para isso.\n")
            if opcao2 == "SIM":
                break # este break é do segundo laço
        print("Voce saiu do segundo laco.")
print("Voce saiu do primeiro laco.")