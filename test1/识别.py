import time
startTime = time.time()*1000
txt='''四十四个字和词,组成一首子、
词、丝的绕口词桃子、李子梨子栗子桔子、
槟子和榛子,栽满院子、村子和寨子。刀子、
斧子、锯子、凿子、锤子、刨子、尺子,做出桌
子、椅子和箱子。名词、动词、数词、代词、量词、
助词、连词,造成语词、诗词和唱词蚕丝生丝、熟丝、缫
丝、晒丝、织丝、自制粗丝、细丝、人造丝'''
list1=[]
list2=[]
t=len(txt)
for i in range(t):
    if '\u4e00'<= txt[i] <= '\u9fff':
         if txt[i] in list1:
             c=list1.index(txt[i])
             list2[c]+=1
         else:
             list1.append(txt[i])
             list2.append(1)
# for i in range(t):
#     for k in range(n):
#         if list2[k]==t-i:
#             list3.append(list1[k])
for i in range(3):
    maxIndex = list2.index(max(list2))
    print(list1[maxIndex])
    list1.pop(maxIndex)
    list2.pop(maxIndex)
    
endtime = time.time()*1000
print(endtime-startTime)