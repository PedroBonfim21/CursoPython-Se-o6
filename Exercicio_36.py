somaQ=0 #soma dos quadrados 
Qsoma=0 #quadrado da soma
for x in range(1,101):
    somaQ+=x**2
    Qsoma+=x
Qsoma=Qsoma**2
result=Qsoma-somaQ
print(f"A diferença entre quadrado da soma e soma dos quadrados é: => {result} <=")
