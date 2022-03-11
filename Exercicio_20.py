parar=False
while parar != True:
    num=int(input("Digite um número: "))
    if num == 1000:
        parar=True
        print("Programa encerrado...")
    if num % 2 == 0:
        print(f"O {num} é par")
    elif num % 2 == 1:
        print(f"O {num} é ímpar")
