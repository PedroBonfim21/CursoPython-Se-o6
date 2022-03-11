num=int(input("Digite um número:"))
for x in range(1, num+1):
    if num % x == 0:
        print(f"Divisores:{x}")
