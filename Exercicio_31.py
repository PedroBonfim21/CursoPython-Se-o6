denominador = 0
resultado = 0
for n in range(1, 100, 2):
    denominador += 1
    divisao = n / denominador
    resultado += divisao
    print(f'{n}/{denominador}', )
print(f'A soma de todos os termos anteriores é igual a {resultado:.2f}')
