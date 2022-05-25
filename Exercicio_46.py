'''
Faça um programa que gera um numero aleatorio de 1 a 1000. O usuario deve tentar acertar qual o numero foi gerado, a cada tentativa o programa devera informar se o chute é menor ou maior que o numero que foi gerado. O programa acaba quando o usuario acerta o numero gerado. O programa deve informar em quantas tentativas o numero foi descoberto
'''
from random import randint

cont=0
aleat=randint(1,1000)
print(aleat)
while True:
    cont+=1
    chute=int(input("Digite seu chute: "))
    print()

    if chute==aleat:
        print("voce acertou, parabens!!!\n")
        print(f"voce acertou na {cont}º tentativa")
        break

    elif chute>aleat:
        print("Chute maior que o valor gerado!\n")

    elif chute<aleat:
        print("Chute menor que o valor gerado!\n")
