import numpy as np

tri = []
for i in range(3):
    tri.append(int(input()))

max = max(tri)
tri.remove(max)

if np.sum(tri) > max:
    if tri[0] == tri[1]:
        if tri[0]**2+tri[1]**2 == max**2:
            print("等腰直角三角形")
        elif tri[0]**2+tri[1]**2 > max**2:
            print("等腰钝角三角形")
        elif tri[0]**2+tri[1]**2 < max**2:
            print("等腰锐角三角形")
        else:
            print('等腰三角形')
    elif tri[0]**2+tri[1]**2 == max**2:
        print("直角三角形")
    elif tri[0]**2+tri[1]**2 > max**2:
        print("钝角三角形")
    elif tri[0]**2+tri[1]**2 < max**2:
        print("锐角三角形")
else:
    print("不能构成三角形")





