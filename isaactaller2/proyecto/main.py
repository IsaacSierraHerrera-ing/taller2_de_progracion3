from clases.animal import Animal
from clases.ave import Ave

ave1 = Ave("LUCHO", 15, 2022, "ISAAC SIERRA")

p = ave1.imprimirnombre()

print(p)

x = ave1.imprimirpropietario()

print(x)

ave1.calcular_edad()