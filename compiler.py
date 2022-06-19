def imformation():
    print("您已进入语法分析器程序")

def getText(name):      #输入文件名，按行读取文件文本，返回一个包含所有行的list数据
    file = open(name,'r',encoding='utf-8')
    try:
        lines = file.readlines()
        # print( "type(lines)=",type(lines)) #type(lines)= <type 'list'>
        # for line in lines:
        #     print( "line=",line  )
    finally:
        file.close()
        return lines

def checkTry(lines):
    cntLine=0
    err=0
    for line in lines:          # 逐行查找try:
        true_Flag=0
        cntLine2=0
        cntLine=cntLine+1
        flag1=line.find('try:')
        if flag1!=-1:
            #print("第{}行try位置：".format(cntLine),flag1)
            for line2 in lines:     # 找到"try:"后,在该行后逐行查找"except"和":"
                flag31=0
                flag32=0
                flag4=0
                cntLine2=cntLine2+1
                # print("cntline=",cntLine)
                # print("cntline2=",cntLine2)
                if cntLine2>cntLine:
                    flag31=line2.find('except',flag1,flag1+len('except'))
                    if flag31!=-1:
                        flag4=line2.find(':',flag31)
                        if flag4 ==-1:
                            print("第{}行语法错误，except后无“：”".format(cntLine),line)
                            err=err+1
                    flag32=line2.find('finally:',flag1,flag1+len('finally:'))
                    #print("except所在位置：",flag31)
                    # print("finally所在位置：",flag32)
                    if flag31!=-1 or flag32!=-1:
                        true_Flag=true_Flag+1
            if true_Flag==0:
                print("第{}行语法错误，无except或finally与try对应".format(cntLine),line)
                err=err+1
    return err      #如果有错误，则返回大于0的值

def checkFor(lines):        
    cntLine=0
    err=0
    for line in lines:          # 逐行查找"for "
        cntLine=cntLine+1
        flag1=line.find('for ')
        if flag1!=-1:
            #print("第{}行for位置：".format(cntLine),flag1)
            flag2=line.find(' in ',flag1+3)         #找到"for "后，在for后查找in
            if flag2==-1:
                print("第{}行语法错误，for后无“in”".format(cntLine),line)
                err=err+1
            else:
                flag3=line.find(':',flag2+4)        #找到"in"后，在for后查找":"
                if flag3==-1:
                    print("第{}行语法错误，for后无“:”".format(cntLine),line)
                    err=err+1
    return err      #如果有错误，则返回大于0的值
    
def checkIf(lines):
    cntLine=0
    err=0
    for line in lines:          # 逐行查找"if "
        true_Flag=0
        cntLine2=0
        cntLine=cntLine+1
        flag1=line.find('if ')
        #print("第{}行if位置：".format(cntLine),flag1)
        if flag1!=-1:
            flag2=line.find(':',flag1+3)    # 找到"if "后，在if后找":"
            if flag2==-1:
                flag3=line.find(' else ')   # 如果if后找不到":",则找"else "
                if flag3==-1:
                    print("第{}行语法错误，if后缺少必要关键字".format(cntLine),line)
                    err=err+1
    return err      #如果有错误，则返回大于0的值

def process():
    menu0 = '''
    本工程可供检索的文件有：
    Da.py
    hesh.py
    menu.py
    seg7.py
    dic.py
    soccer_manager.py
    url.py
    compiler.py
    您也可以根据需求向工程目录中添加自定义的txt或者py文件
    请输入需要编译的文件名："
    '''
    while True:
        try:
            name=input(menu0)
            lines=getText(name)      #输入文件名，按行读取文件文本，返回一个包含所有行的list数据
            break
        except Exception:
            print("输入错误！请重新输入")
    print("开始判断三种语法......")   
    a=checkTry(lines)
    b=checkFor(lines)
    c=checkIf(lines)
    s=a+b+c
    return s      #如果有错误，则返回大于0的值

def summary(s):
    if s>0:
        print("编译完成，程序有语法错误请修改")
    else:
        print("编译完成，程序无语法错误")
    return 0

def run_compiler():
    imformation()
    s=process()
    summary(s)
    return 0
