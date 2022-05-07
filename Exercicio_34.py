from math import gcd
numeros = range(2, 21)
def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m
print(mmc(numeros))
