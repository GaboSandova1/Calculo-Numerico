#Gabriel Sandoval    Ci:30.866.625
#Anaconda:
import numpy as np

def is_symmetric(mat):
    return np.allclose(mat, mat.T)

def doolittle(mat):
    n = len(mat)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            s1 = sum(L[i][k]*U[k][j] for k in range(j))
            if i == j:
                L[i][i] = 1
                U[i][i] = mat[i][i] - s1
            else:
                U[i][j] = mat[i][j] - s1
    
    return L, U

def choleski(mat):
    n = len(mat)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            s1 = sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                L[i][i] = np.sqrt(mat[i][i] - s1)
            else:
                L[i][j] = (mat[i][j] - s1) / L[j][j]
    
    return L

def test_methods():
    mat = np.array([[4, 2, -2], [2, 10, -5], [-2, -5, 14]])
    print("Matriz de prueba:")
    print(mat)
    
    if is_symmetric(mat):
        print("\nDescomposición de Doolittle:")
        L, U = doolittle(mat)
        print("Matriz L:")
        print(L)
        print("Matriz U:")
        print(U)
        
        print("\nDescomposición de Choleski:")
        L = choleski(mat)
        print("Matriz L:")
        print(L)
    else:
        print("La matriz ingresada no es simétrica. Solo se puede aplicar el método de Choleski.")
        print("\nDescomposición de Choleski:")
        L = choleski(mat)
        print("Matriz L:")
        print(L)

test_methods()




#Vscode:

def dec2bin(n, num_bits):
    bin_n = bin(n)[2:]
    return bin_n.zfill(num_bits)

def dec2oct(n):
    oct_n = oct(n)[2:]
    return oct_n

def dec2hex(n):
    hex_n = hex(n)[2:]
    return hex_n

while True:
    try:
        n = int(input("Ingrese un número entero positivo: "))
        break
    except ValueError:
        print("Numero invalido, por favor ingrese un número decimal.")

num_bits = int(input("Ingrese el número de bits para la representación binaria: "))

print("\nLos resultados en diferentes bases numéricas son:")
print(f"Binario: {dec2bin(n, num_bits)}")
print(f"Octal: {dec2oct(n)}")
print(f"Hexadecimal: {dec2hex(n)}")
