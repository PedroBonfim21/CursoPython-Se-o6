'''
Leia um numero positivo do usuario, entao, calcule e imprima a sequencia de fibonacci até o primeiro numero superior ao numero lido. Exemplo: se o usuario informou o numero 30, a sequencia a ser impressa será 0 1 1 2 3 5 8 13 21 34.
'''
num=int(input("Digite um numero: "))
t1=0
t2=1
print(f"{t1}-{t2}",end='')
while True:
    t3=t1+t2
    t1=t2
    t2=t3
    print(f"-{t3}",end='')
    if num<t3:
        break
