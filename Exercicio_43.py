'''
Faça um programa que leia um numero indeterminado de idade dos individuos (pare quando for informada a idade 0), e calcule a media da idade desse grupo.
'''
cont=media=0
while True:
    idade=int(input("Digite a idade: "))
    if idade>0:
        cont+=1
        media+=idade

    else:
        break

mediaS=media/cont
print()
print(f"media igual a: {mediaS} ")
print()
print(f"Numeros de idades e igual a: {cont} ")