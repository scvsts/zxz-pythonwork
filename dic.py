import keyword
keyList = keyword.kwlist
def getText(name):
    txt = open(name, "r",encoding='utf-8').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt

def run_dic():
    try:
        name=input("目前支持查找的文件有：\nDa.py\nhesh.py\nmenu.py\nseg7.py\ndic.py\nsoccer_manager.py\nurl.py\ncompiler.py\n0.返回上一级")
        if name==0:
            return 0
        else:
            keyTxt = getText(name)
            words  = keyTxt.split()
            counts = {}
    except Exception:
        print("输入错误！请输入正确的文件名")
        return 0 
    for word in words:			
        if word in keyList:
            counts[word] = counts.get(word,0) + 1  
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True) 
    try:
        print ("检查结果为:")
        for i in range(33):
            word, count = items[i]
            print ("{0:<10}{1:>5}".format(word, count))
    except IndexError:
        print ("{0:<10}{1:>5}".format(word, count))
    return 0