def soma_diagonalsecundaria(A):

    soma = 0

    i = 0
    j = len(A)-1

    while j >= 0:
        soma += A[i][j]

        i += 1
        j -= 1
    
    return soma