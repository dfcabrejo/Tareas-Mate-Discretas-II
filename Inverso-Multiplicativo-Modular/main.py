import math


def mcd(m, n):
    c = math.trunc(m / n)
    r = m - (c * n)
    while r != 0:
        m = n
        n = r
        c = math.trunc(m / n)
        r = m - (c * n)
    return n


def inverso_multiplicativo(a, n):
    if a == 0:
        return 0, 1
    else:
        x, y = inverso_multiplicativo(n % a, a)
        return y - (n // a) * x, x


def hallar_inverso(a, n):
    if mcd(a, n) == 1:
        x, y = inverso_multiplicativo(a, n)
        return x
    else:
        return f'No existe el inverso multiplicativo, el máximo común divisor es {abs(mcd(a, n))}'


print(hallar_inverso(7, 160))


