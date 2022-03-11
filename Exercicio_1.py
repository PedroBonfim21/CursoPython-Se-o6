num = 0
lista = []
for x in range(0,30):
    if x%3==0 and x>0:
        if num <=4:
            lista.append(x)
            num+=1
        else:
            break
print(f"Os primeiros 5 números múltiplos de 3 são {lista}")