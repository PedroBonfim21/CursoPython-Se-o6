'''
Faça um programa que calcula a associação em paralelo de resistores R1 e R2 fornecidos pelo usuario via teclado. O programa fica pedindo estes valores e calculando até que o usuario entre com um valor para resistencia igual a zero.

R=(R1*R2)/(R1+R2)

'''
while True:
    
    R1=int(input("Digite o valor do Resistor 1: "))
    R2=int(input("Digite o valor do Resistor 2: "))
    print()
    
    if R1==0:
        if R2==0:
            print("Digite outro valor para R2 pois os dois nao podem ser iguais a zero")
            R2=int(input("Digite o valor do Resistor 2: "))
    
    R=(R1*R2)/(R1+R2)
    
    print(f"O valor da resistencia é: {R}")
    
    if R==0:
        break
    else:
        print("Digite outro valor, pois o valor da resistencia nao é igual a zero\n")
