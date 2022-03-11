maior = menor=0

for x in range(1, 11):
    num = int(input(f'informe um {x}/10 numero: '))
    if x==1:
        menor=num
        maior=num
    else:
        if num > maior:
                maior = num
        if num < menor:
                menor = num
print(f'menor numero = {menor}')
print(f'maior numero = {maior}')