with open("Answer3.txt",'w') as aw3:
    count = len(open('test.py', 'r').readlines())
    file = open('test.py', 'r')
    strList = file.readlines()
    maxEle = 0
    for i in strList:
        if len(i) > maxEle:
            maxEle = len(i)
    num = 1
    for i in range(count):
        ele = strList[i][:-1] + ' '*(maxEle-len(strList[i])) + '#' +str(i)
        aw3.write(ele+'\n')
