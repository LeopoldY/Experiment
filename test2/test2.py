weekDic = {
    1:'Sun',
    2:'Mon',
    3:'Tues',
    4:'Wed',
    5:'Thur',
    6:'Fri',
    7:'Sat'
}

def TravelCase(tempretureList:list,minTemp):
    for i in range(5):
        if tempretureList[i] > minTemp and tempretureList[i+1] > minTemp and tempretureList[+2] > minTemp:
            print(f'{weekDic[i+1]},{weekDic[i+2]},{weekDic[i+3]} are suitable for traveling.')

if __name__ == '__main__':
    weekTemp = []
    for i in range(7):
        weekTemp.append(input(f'The tempreture of {weekDic[i+1]}:'))
    minTemp = input('The minimun tempreture:')
    TravelCase(weekTemp,minTemp)