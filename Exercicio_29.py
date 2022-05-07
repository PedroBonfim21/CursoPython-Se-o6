n=int(input("Digite um número: "))
soma = 0
soma2 = 3
soma3 = 0
for x in range(1, n+1):
    soma += x
print(soma)
for y in range(1, (2*n)):
    soma2+=y
print(soma2)
for z in range(1,(2*n),2):
    soma3+=z
print(soma3)
