def produto_interno():

    produtointerno = 0
    #produtointerno = []
    while True:
        print("Insira o primeiro vetor:")
        A = eval(input())
        print("Insira o segundo vetor:")
        B = eval(input())
        
        if(len(A)!= len(B)):
            print("O produto não pode ser realizado entre vetores de tamanho diferente.")
            continue
        
        else:
            for i in range(len(A)):
                aux = A[i] * B[i]

                produtointerno += aux
                #produtointerno.append(aux)

        return produtointerno
           
print(produto_interno())