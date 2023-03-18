#instalamos e importamos la libreria numpy de python
import numpy as np


#algoritmo paso hacia atras
def backward_substitution(U, b):
    n = len(b)
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= U[i][j]*x[j]
        x[i] /= U[i][i]
        
    return x


#algoritmo, paso hacia adelante

def forward_substitution(L, b):
    n = len(b)
    x = np.zeros(n)
    
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= L[i][j]*x[j]
        x[i] /= L[i][i]
        
    return x





#pruebas
U = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

b = np.array([7.85, -19.3, 71.4])

x = backward_substitution(U, b)

print(x)