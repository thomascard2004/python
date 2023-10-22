def produto_interno():
    '''retorna o produto interno de dois vetores de mesmo tamanho.'''
#trocando o comentários pela linha de código logo acima dos respectivos, o função pode retornar uma lista com o produto dos números nas mesmas posições.

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