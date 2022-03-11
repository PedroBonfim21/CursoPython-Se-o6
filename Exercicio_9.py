num = int(input("Digite um número inteiro:"))
for impar in range(num):
    if impar % 2 == 1:
        print(f"{impar} é um número ímpar menor que {num}")
        
