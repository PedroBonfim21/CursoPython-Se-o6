x=float(input("Digite o salario de carlos: "))

carlos=x
joao=x/3
cont=0

while True:
    if joao<carlos:
        carlos += carlos*0.02
        joao += joao*0.05
        cont+=1
    else:
        print("encerrado")
        print("Aplic de carlos : ({%.2f})" %carlos)
        print("Aplic de joao : ({%.2f})" %joao)
        print(f"Quantidade de meses: ({cont})")
        break