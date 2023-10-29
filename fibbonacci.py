#esse código recebe um número e printa a lista de fibbonacibonacci até o respectivo número

num = int(input("Digite um número: "))
fibbonaci = [0,1]
somatotal = 1

if num == 0:
    fibbonaci = [0]
    somatotal = 0
    
for i in range (num):
    somaaux = fibbonaci[len(fibbonaci)-1] + fibbonaci[len(fibbonaci)-2] 
    if somaaux > num:
        break
    fibbonaci.append(somaaux)
    somatotal += somaaux

print(fibbonaci)   
print("A soma de todos os números inclusos nessa lista é: "+ str(somatotal))