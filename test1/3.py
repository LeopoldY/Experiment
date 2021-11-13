def count_words(s, n):
    dic = {}
    for i in s:
        if '\u4e00' <= i <= '\u9fff':
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    # top = sorted(w.items(), key=lambda item:(-item[1], item[0]))
    # top_n = top[:n]
    # return top_n
    return dic

str1='''四十四个字和词,组成一首子、
词、丝的绕口词桃子、李子梨子栗子桔子、
槟子和榛子,栽满院子、村子和寨子。刀子、
斧子、锯子、凿子、锤子、刨子、尺子,做出桌
子、椅子和箱子。名词、动词、数词、代词、量词、
助词、连词,造成语词、诗词和唱词蚕丝生丝、熟丝、缫
丝、晒丝、织丝、自制粗丝、细丝、人造丝'''
list1=[]
strDic = count_words(str1, 3)
ans = [(v, k) for k, v in strDic.items()]
ans = sorted(ans,reverse=True)
print(ans)