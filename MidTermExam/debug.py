fn = lambda *p:print(p[1]+p[2]+'|',end='')

def fun(n,x,y,z):
    if n == 1:
        fn(1,x,y)
    else:
        fun(n-1,x,z,y)
        fn(1,x,y)
        fun(n-1,z,y,x)

fun(3,'A','B','T')