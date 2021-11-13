num = lambda n,k:str(n)[-k] if k<=len(str(n)) else -1

print(num(123,3))



isExist = lambda d,n:True if list(str(n)).index(str(d)) != '\0' else False

print(isExist(10,100))