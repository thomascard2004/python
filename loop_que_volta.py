while True:
    print("Digite um número:")
    num = int(input())

    if num < 0 or num > 10:
        continue
    else:
        print(num)
        break