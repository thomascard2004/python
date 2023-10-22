#esse código recebe uma quantidade de salários e retorna qual deles é o maior.
print("Quantos salários deseja conferir?")
numsal = int(input())


maiorsal = 0
for i in range (numsal):
    print("Digite o salário bruto (R$):")
    sal = float(input())

    if(sal > maiorsal):
        maiorsal = sal

print (maiorsal)        