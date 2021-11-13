import math

def cosAlpha(x):
    return x/deno

def cosBeta(y):
    return y/deno

def cosGamma(z):
    return z/deno

if __name__ == '__main__':
    x = int(input('x:'))
    y = int(input('y:'))
    z = int(input('z:'))
    deno = math.sqrt(x**2+y**2+z**2)
    print(f'cosAlpha:{cosAlpha(x)},cosBeta:{cosBeta(y)},cosGamma:{cosGamma(z)}')