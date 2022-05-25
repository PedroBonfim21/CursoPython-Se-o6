'''
Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e raiz quadrada. Finalize a entrada de dados com um numero negativo ou zero.
'''
while True:
    num=int(input("Digite um número: "))

    if num>0:
        print()
        print(f"O quadrado de {num} e igual a: {num**2} ")
        print(f"o cubo de {num} e igual a: {num**3} ")
        print(f"A raiz quadrada e igual a: {num**(1/2)}\n")

    else:
        print("Programa encerrado, numero menor que zero")
        break

    