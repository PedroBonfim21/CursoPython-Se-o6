num=int(input("Digite um número par: "))
soma= 0
while num % 2 == 1:
    num=int(input("Esse não é um número par.\nDigite um número par: "))
for x in range(0, num+1):
    soma += x
print(soma)