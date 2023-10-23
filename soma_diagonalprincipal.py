#um programa que imprime a soma da digonal principal de uma matriz da forma ([[0,0,0],[0,0,0]])
def soma_diagonalprincipal(A):
    soma = 0

    for i in range(len(A)):
        for j in range(len(A)):
            if( i == j):
                soma += A[i][j]

    return soma