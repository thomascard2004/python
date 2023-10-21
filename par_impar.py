print("Quantos números deseja analisar?")
quantnum = int(input())
par = 0
impar = 0

for i in range(quantnum):
    print("Digite um número:")
    num = int(input())

    if (num % 2 == 0):
        par += 1
    else:
        impar += 1 

print(str(par)+" Números pares")
print(str(impar)+" Números impares:")        