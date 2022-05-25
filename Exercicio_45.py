'''
Faça um algoritimo que converta a velocidade expressa em Km/h para M/s e vice versa. voce deve criar um menu com as duas opções de conversão e uma opção para finalizar o programa. O usuario podera fazer quantas conversões desejar, sendo que o programa so sera quando a opção de finalizar for escolhida.
'''
linhas='-'*43

print(f"{linhas}\n")
print("Digite 1,2 ou 3 para selecionar a opção:\n")
print("1-Converter M/s em Km/h\n2-Converter Km/h em M/s\n3-Encerrar o programa\n")
print(f"{linhas}\n")

while True:
    opc=int(input("Digite 1,2 ou 3 para selecionar a opção: "))
    print()

    if opc==1:
        km_h=float(input("Digite o valor em Km/h: "))
        Ms=km_h/3.6
        print(f"O valor em M/s e: {Ms} M/s\n")

    elif opc==2:
        Ms=float(input("Digite o valor em M/s: "))
        km_h=Ms*3.6
        print(f"O valor em Km/h e: {km_h} Km/h\n")

    elif opc==3:
        print("Programa encerrado")
        break

    else:
        print("Opção invalida, digite um dos numeros a baixo: ")
