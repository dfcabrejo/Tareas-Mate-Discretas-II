import math
from fuerzabruta import mcd, euler_totient


def es_primo(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    if divisores == [1, n]:
        # print('Es primo')
        return True
    else:
        # print('No es primo')
        return False


def factores_primos(num):
    fact_primos = []
    multiplicacion = 0
    cociente = num
    divisor = 2
    while cociente > 1:
        if cociente % divisor == 0 and es_primo(divisor) is True:
            fact_primos.append(divisor)
            cociente = cociente / divisor
            divisor = 2
        else:
            divisor += 1

    return fact_primos


def euler_totient_lema(x):
    if x == 1:
        return 0
    else:
        descomposicion = factores_primos(x)
        factores = []
        exponentes = []
        totient = 1
        for item in descomposicion:
            if item not in factores:
                factores.append(item)
                exp = 0
                for num in descomposicion:
                    if num == item:
                        exp += 1
                exponentes.append(exp)
        for pos in range(0, len(factores)):
            p = factores[pos]
            a = exponentes[pos]

            totient = totient * ((p ** a) - (p ** (a - 1)))

        return totient