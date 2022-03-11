from math import factorial

const=1
soma=0
num=int(input("Digite um número: "))
for x in range(1, num+1):
    soma= soma + (const/factorial(x))
print(soma)
