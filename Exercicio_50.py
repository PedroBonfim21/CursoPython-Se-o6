chico=1.50
ze=1.10
cont=0

while True:
    if ze<chico:
        chico += 0.02
        ze += 0.03
        cont+=1
    else:
        print("Aplic de chico : %.2f" %chico)
        print("Aplic de ze : %.2f" %ze)
        print(f"Quantidade de anos: ({cont})")
        break