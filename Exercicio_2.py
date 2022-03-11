num_w=1
num_dw=1

loop=str.title(input("Digite o tipo de Loop desejado (For, While ou Dowhile):\n "))
print(f"o loop escolhido foi {loop}")
if loop=="For":
    for x in range(1,101):
        print(x)
elif loop=="While":
    while num_w <101:
        print(num_w)
elif loop=="Dowhile" or "DoWhile":
    while True:
        print(num_dw)
        num_dw+=1
        if num_dw==101:
            break
else:
    print("Loop inexistente")
