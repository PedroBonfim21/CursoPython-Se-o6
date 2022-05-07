limite=int(input("Digite a quantidade de números que ira a parecer: "))
i=int(input("Digite os números: ")) 
j=int(input("Digite os números: "))
lista=[]
x=0
while len(lista)<limite:#pegando o número de elementos na lista e comparando com o limite
    if(x%i == 0 or x%j == 0):#definindo se são ou nao multiplos
        lista.append(x)#adicionando aqueles q são multiplos
    x+=1#adicionando e conferindo se são multiplos
print(lista)#[0,2,3,4,6,8] caso, i=2;j=3;limite =6

