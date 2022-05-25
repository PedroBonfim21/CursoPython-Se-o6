'''
Faça um programa que calcule a area de um triangulo, cuja base e altura sao fornecidas pelo usuario. Esse programa nao pode permitir a entrada de dados invalidos, ou seja, medidas menores ou iguais a 0.
'''
x=0
while (x!=1):
    base = int(input("Digite o tamanho da base do triângulo: "))
    if base > 0:
        altura = int(input("Digite o tamanho da altura do triângulo: "))
        if altura > 0:
            area_triangulo = (base * altura) / 2
            print(f"A aréa do triângulo é {area_triangulo}")
            x+=1
        else:
            print("Altura inválida! Digite outro valor para a altura\n")
    else:
        print("Base inválida! Digite outro valor para a base\n")
