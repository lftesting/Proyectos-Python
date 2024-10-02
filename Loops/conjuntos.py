# para conjuntos se utilizan {}
A={1,2,3,4}
B={2,3,5,6}
C={3,4,6,7}

# | para unir todos los valores en cada conjunto
print(A|B)
print(A|C)
print(B|C)

# para hacer interseccion de conjuntos usar &
print(A&B)
print(A&C)
print(B&C)

#para diferencia de conjuntos usar signo - (menos)
print(A-B)

# para diferencia asimetrica ^ (todos los componentes que estan en algun conjunto pero no en ambos)
print(A^B)
