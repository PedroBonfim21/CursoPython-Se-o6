'''
faça um programa que aprensente um menu de opções para o calculo das seguintes operações entre dois numeros:
adição--subtração--multiplicação--divisão--saída
O programa deve possibilitar ao usuarioa escolha da operação desejada, a exibição do resultado e a vota ao menu de opções. O programa só termina quando o for escolhida a opção de saída (opção 5).
'''
linhas='-'*43
while True:
    print(f"{linhas}\n")
    print("Digite 1,2,3,4 ou 5 para selecionar uma opção:\n")
    print("1- Adicao \n2- Subtracao \n3- Multiplicacao \n4- Divisao \n5- Saida \n")
    print(f"{linhas}\n")
    opc=int(input("Selecione uma das opcoes acima: "))
    if opc==1:
        print()
        print("Nao selecionou a opcao certa e quer voltar ao menu anterior?\n ")
        print("Se sim, Digite ('0')\nCaso queira continuar com a opcao selecionada selecionada no menu digite ('9'): )",end='')
        conferir=int(input(":"))
        if conferir == 0:
            print()
        elif conferir == 9:
            print()
            print("opcao selecionada: ADICAO(+)")
            num1=int(input("Digite o numero: "))
            num2=int(input("Digite o numero: "))
            soma=num1+num2
            print(f"O resultado foi: {soma}")
    elif opc==2:
        print()
        print("Nao selecionou a opcao certa e quer voltar ao menu anterior?\n ")
        print("Se sim, Digite ('0')\nCaso queira continuar com a opcao selecionada selecionada no menu digite ('9'): )",end='')
        conferir=int(input(":"))
        if conferir == 0:
            print()
        elif conferir == 9:
            print()
            print("Opção selecionada: SUBTRACAO(-)")
            print("OBS:Caso nao queira um resultado negativo coloque o maior numero primeiro")
            num1=int(input("Digite o numero: "))
            num2=int(input("Digite o numero: "))
            subtr=num1-num2
            print(f"O resultado foi: {subtr}")
    elif opc==3:
        print()
        print("Nao selecionou a opcao certa e quer voltar ao menu anterior?\n ")
        print("Se sim, Digite ('0')\nCaso queira continuar com a opcao selecionada selecionada no menu digite ('9'): )",end='')
        conferir=int(input(":"))
        if conferir == 0:
            print()
        elif conferir == 9:
            print()
            print("Opção selecionada: MULTIPLICACAO(*)")
            num1=int(input("Digite o numero: "))
            num2=int(input("Digite o numero: "))
            multipl=num1*num2
            print(f"O resultado foi: {multipl}")
    elif opc==4:
        print()
        print("Nao selecionou a opcao certa e quer voltar ao menu anterior?\n ")
        print("Se sim, Digite ('0')\nCaso queira continuar com a opcao selecionada selecionada no menu digite ('9'): )",end='')
        conferir=int(input(":"))
        if conferir == 0:
            print()
        elif conferir == 9:
            print()
            print("Opção selecionada: DIVISAO(/)")
            num1=int(input("Digite o numero dividendo: "))
            num2=int(input("Digite o numero divisor: "))
            div=num1/num2
            print(f"O resultado foi: {div}")
    elif opc==5:
        print("Programa encerrado")
        break
