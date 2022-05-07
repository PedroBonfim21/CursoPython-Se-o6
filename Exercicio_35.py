inicial=int(input("Digite o limite inicial: "))
final=int(input("Digite o limite final: "))
soma=0
for x in range(inicial, final+1):
    if x%2==1:
        soma+=x
print(soma)
