soma=0
multi=1
num1=float(input("1º Digite um número: "))
num2=float(input("2º Digite um número: "))
if num1 < num2:
    for n in range(num1,num2+1):
        if n % 2 == 0:
            soma += n
        if n % 2 == 1:
            multi *= n
elif num2 < num1:
    for n in range(num2,num1+1):
        if n % 2 == 0:
            soma += n
        if n % 2 == 1:
            multi *= n
print(f"A soma dos números pares entre os números citados é {soma}")
print(f"e a multiplicação dos números ímpares é {multi}")
