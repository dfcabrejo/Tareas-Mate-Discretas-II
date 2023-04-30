from lema import euler_totient_lema
from fuerzabruta import euler_totient
from timeit import timeit

fuerza_bruta_tiempo = timeit(lambda: euler_totient(1234561), number=1)
lema_tiempo = timeit(lambda:euler_totient_lema(1234561), number=1)
print(fuerza_bruta_tiempo, lema_tiempo)
