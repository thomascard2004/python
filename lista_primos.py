def Eh_primo(num):

    pontos = 0
    for i in range(2, num):
        if (num % i == 0):
            pontos += 1

    if(pontos >= 1):
        return False
    else:
        return True

limite = int(input())
listaprimos = []

for i in range(2,limite):
    if (Eh_primo(i)):
        listaprimos.append(i)

print(listaprimos)