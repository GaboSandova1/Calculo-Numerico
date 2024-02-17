#Gabriel Sandoval   Ci:30.866.625
#Ejercicio 1

import numpy as np

def metodo_potencia_simetrico(matriz, iteraciones):
    n = len(matriz)
    x = np.random.rand(n)
    x = x / np.linalg.norm(x)
    for _ in range(iteraciones):
        y = np.dot(matriz, x)
        x = y / np.linalg.norm(y)
        
    eigenvalor = np.dot(x, np.dot(matriz, x))
    eigenvector = x
    return eigenvalor, eigenvector

matriz_simetrica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
iteraciones = 1000
eigenvalor, eigenvector = metodo_potencia_simetrico(matriz_simetrica, iteraciones)

print("Eigenvalor aproximado mas grande: ", eigenvalor)
print("Eigenvector correspondiente aproximado: ", eigenvector)

