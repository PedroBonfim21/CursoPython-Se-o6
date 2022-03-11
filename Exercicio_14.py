num=int(input("Digite um número par: "))
while num%2==1:
    num=int(input("Esse não é um número par.\nDigite um número par: "))
for x in range(num,-1,-2):
    print(x)
