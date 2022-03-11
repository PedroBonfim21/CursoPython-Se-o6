soma=0
num=int(input("Digite um número inteiro"))
for x in range(1, num):
    if num % x == 0:
        print(x)
        soma += x
print(f"A soma é {soma}")
