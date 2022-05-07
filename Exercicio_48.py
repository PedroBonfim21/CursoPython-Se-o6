t1 = 0
t2 = 1
soma = 0
while True:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3)
    if t3 > 4000000:
        break
    elif t3 % 2 == 0 and t3 < 4000000 and soma < 4000000:
        soma = soma + t3
print(f"A soma é: {soma}")
