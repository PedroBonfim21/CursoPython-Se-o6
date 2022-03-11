soma = 0
for i in range(1, 11):
    n = int(input(f'informe um {i}/10 numero: '))
    while n < 0:
        print("informe um numero positvo")
        n = int(input(f'informe um {i}/10 numero: '))
    soma = soma + n
media = soma/10
print(media)

