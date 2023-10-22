def multiplicar_Matrizes(A,B):
    '''retorna a multiplicação entre duas matrizes da forma [[0,0,0],[0,0,0]...]'''
    num_linhasA, num_colunasA = len(A), len(A[0])
    num_linhasB, num_colunasB = len(B), len(B[0])

    matrizresultado = []

    if (num_colunasA != num_linhasB):
        print("As matrizes não podem ser multiplicadas")

    else:
        matrizresultado = [[0]*num_colunasB for _ in range(num_linhasA)]

        for i in range(num_linhasA):
            for j in range(num_colunasB):
                for k in range(num_linhasB):
                    matrizresultado[i][j] += A[i][k] * B[k][j]
    
    
    return matrizresultado