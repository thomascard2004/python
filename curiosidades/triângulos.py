lado1 = float(input())

lado2 = float(input())

lado3 = float(input())

if(lado1 < 0 or lado2 < 0 or lado3 < 0):
    raise ValueError("Lado não pode ser negativo!")
    
elif((lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2+lado3) < lado1):
    raise ValueError("Um lado não pode ser maior que a soma dos outros dois")

if( lado1 == lado2 == lado3):
    print("equilátero")
    
elif (lado1 == lado2 != lado3):
    print("isóceles")

elif(lado1 != lado2 != lado3):
    print("escaleno")
  