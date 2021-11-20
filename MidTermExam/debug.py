import math
x = float(input())

def sqrtN(x,n):
    for _ in range(n):
        x = math.sqrt(x)
    return x

if x > 10:
    y = math.sin(x) + math.sqrt(x**2+1)
elif 0 < x and x <= 10:
    y = math.e ** x + sqrtN(x,5)
elif x <= 0:
    y = math.cos(x) - x**3 + 6*x

print('%.2f'%y)