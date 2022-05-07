validos=[]
for num in range(1000,10000):
    prim=num // 100
    seg= num % 100
    soma=prim+seg
    pot=soma**2
    if pot==num:
        validos.append(num)
print(validos)
