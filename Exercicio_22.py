bool=True
soma=0
cont=0
while bool:
    nota = 10
    while 10 >= nota <= 20:
        nota = float(input("Digite a nota: "))
        if nota > 20:
            break
        soma+=nota
        cont+=1
    if nota > 20:
        bool = False
print(f"A média é: {soma/cont}")
