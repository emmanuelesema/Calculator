import math

def add(x, y):
    z = float(x) + float(y)
    return round(z,2)

def divide(x, y):
    z = x/y
    return z

def factorial(x):
    z=1
    if x < 0:
        raise ValueError("Value is below zero")
    elif x == 0:
        return z
    else:
        for i in range(1, x + 1):
            z = z*i
    return z
    
def sin(x):
    N = 20
    z = 0
    for i in range(N+1):
        z += (-1)**i * x**(2*i + 1)/(math.factorial(2*i + 1))
    return round(z,2)