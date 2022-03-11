num=int(input("Digite um número ímpar: "))
while num%2==0:
    num=int(input("Esse não é um numero ímpar.\nDigite um número ímpar: "))
for x in range(1,num+1):
    if x % 2 == 1:
        print(x)