soma=0
conta=0
for x in range(1,11):
     n=int(input(f"Digite o {x}°número: "))
     soma+=n
     conta+=n
media=soma/conta
print(f"A média sntre os 10 números é igual a: {media}")