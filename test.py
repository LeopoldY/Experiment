num = lambda n,k:str(n)[-k] if k<=len(str(n)) else -1

print(num(123,3))



isExist = lambda d,n:True if str(d) in str(n) else False

print(isExist(0,100))


