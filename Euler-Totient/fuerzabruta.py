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


def euler_totient(n):
    totient = 0
    for num in range(1, n):
        a = mcd(num, n)
        if a == 1:
            totient += 1
    return totient
