l = float(input("Qual a largura da parede em metros:"))
a = float(input("Qual a altura da parede em metros:"))
m = (l * a)
t = (l * a) / 2
print("A parede tem {}m², sendo assim gastara {:.1f}L de tinta".format(m, t))