'''
Elabore um programa que faça a leitura de varios numeros inteiros, ate que se digite um numero negativo. O programa tem que retornar o maior e o menor numero lido.
'''
cont=maior=menor= 0
while (cont!=1):
    num=int(input("Digite um numero: "))
    if num>=0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num    
    else:
        cont=1
        print("Programa encerrado")
print(f"O menor número digitado é {menor}")
print(f"O maior número digitado é {maior}")
