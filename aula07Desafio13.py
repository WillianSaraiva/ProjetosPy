sal = float(input("Digite seu salario R$ "))
Aum = (15 * sal) / 100
aum = sal + Aum
imp = (27.5 * aum) / 100
print("Salario antigo R$ {:.2f}. \nNovo salario com aumento de 15% e R$ {:.2f}. "
      "\nSalario com desconto de imposto R$ {:.2f}.".format(sal, aum, (aum-imp)))