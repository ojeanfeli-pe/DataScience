import numpy

print("Criando um matriz a partir de uma lista:")
l = [[3,4,5], [6,7,8],[9,0,1]]
z = numpy.matrix(l)
print (z)
#CONFERINDO OS DADOS PARA VER SE O RESULTADO E ESSE:
# [3 4 5]
# [6 7 8]
# [9 0 1]
print("Transporta da matriz: ")
print(z.T)
#CONFERINDO OS DADOS PARA VER SE O RESULTADO E ESSE:
# [3 6 9]
# [4 7 9]
# [5 8 1]
print("Inversa da matriz:")
print(z.I)
#[[-0.33333333 1. -1. ]
#[-2.1 -1.2 0.1]]
#Criando outra matriz
R = numpy.matrix([[3,2,1]])
print("Multiplicando matrizes:")
print(R * z)
#[[30 26 32]]

print("Resolvendo um sistema linea:")
print (numpy.linalg.solve(z, numpy.array([0,1,2])))

from numpy import *
#Matriz 3x3
A = array([(9,4,2), (5,3,1),(2,0,7)])
print("Matriz A:")
print (A)
#Decompondo usando QR
Q, R = numpy.linalg.qr(A)
#Resultados
print("Matriz Q:")
print(Q)
print("Matriz R:")
print(R)

#Produto
print("Q.R:")
print(numpy.dot(Q,R))