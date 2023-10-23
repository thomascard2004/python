#esse código provê uma lista de contatos de memória ram, ou seja, os contatos não ficam salvos quando o programa é fechado e reaberto.
import os
contatos = {}


while True:
    os.system('clear')
    print("Digite qual operação deseja realizar: \n\n 1-Cadastrar Contatos \n\n 2-Listar Contatos \n\n 3-Limpar lista de Contatos \n\n 4-Sair")
    op = int(input())

    if(op == 1):
        os.system('clear')
        print("Digite o nome do contato:")
        nome = input()

        print("Digite o número do contato:")
        numero = input()

        contatos[nome] = numero
        
    elif(op == 2):
        os.system('clear')
        print(contatos)
        input()

    elif(op == 3):
        contatos.clear()
        os.system('clear')
        print("A lista de contatos foi limpa.")
        input()

    elif(op == 4):
        os.system('clear')
        print("Tchauzinho!!")
        break
    
    else:
        os.system('clear')
        print("A opção digitada é inválida, tente novamente:")
        input()
