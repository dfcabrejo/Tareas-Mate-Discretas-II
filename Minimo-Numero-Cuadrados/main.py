from math import sqrt

def min_cuadrados(n):
    cuenta=n
    contador_cuadrados = 0
    num=n
    cuadrados=[]
    while cuenta > 0:
     root = sqrt(num)
     if root.is_integer():
       contador_cuadrados+=1
       cuenta -= num
       cuadrados.append(num)
       num=cuenta
     else:
       num-=1
    print(contador_cuadrados, cuadrados)

min_cuadrados(46)
