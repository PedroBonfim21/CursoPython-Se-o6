num=int(input("Digite um número par: "))
while num % 2 == 1:
    num=int(input("Esse não é um número par.\nDigite um número par: "))
for x in range(0, num+1):
    if x % 2 == 0:
        print(x)