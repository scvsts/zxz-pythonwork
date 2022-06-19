import turtle
from logging import exception
from operator import truediv
def pen_init(pythonsize,penColor,speed):
    turtle.setup(0.5,0.5,0,0)        #前两位：设置窗体大小，宽高为整数时为像素，小数为所占比例。
                                                  #后两位：设置窗口左顶点位置，都为空则是在中间      
    turtle.pensize(pythonsize)
    turtle.color(penColor)
    turtle.speed(speed)                    #启动爬行的方向
    turtle.penup()                    #启动爬行的方向
    return 0

def drawHeng(size,startX1,startY1):
    turtle.goto(startX1,startY1)
    turtle.seth(0)  
    turtle.pendown() 
    scale=50
    for i in range(17):
        a='*'   *i
        b='.'*(scale - i)
        c=(i/scale)*100
        turtle.fd(size//16)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')
    turtle.penup()
    return 0
    
def drawPie(size,startX2,startY2):
    turtle.goto(startX2,startY2)
    turtle.seth(-90)  
    turtle.pendown() 
    scale=50
    for i in range(10):
        j=i+17
        a='*'   *j
        b='.'*(scale - j)
        c=(j/scale)*100
        turtle.fd(size//27)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')
        
    for i in range(10):
        k=i+27
        a='*'   *k
        b='.'*(scale - k)
        c=(k/scale)*100
        turtle.circle(-size//2,8)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')
    turtle.penup()
    return 0

def drawNa(size,startX3,startY3):
    turtle.goto(startX3,startY3)
    turtle.seth(-90)  
    turtle.pendown() 
    scale=50
    for i in range(14):
        j=i+37
        a='*'   *j
        b='.'*(scale - j)
        c=(j/scale)*100
        turtle.circle(size//2,5)
        print("\r [{}-{}]{:^3.0f}%".format(a,b,c),end='')
    turtle.penup()
    return 0

def drawDa(size,startX,startY):
    startX1,startY1=startX-size/2,startY
    startX2,startY2=startX,startY+size/4
    startX3,startY3=startX,startY-size*0.1
    drawHeng(size,startX1,startY1)
    drawPie(size,startX2,startY2)
    drawNa(size,startX3,startY3)
    return 0

def printIntro():
    print("您已进入绘图程序，程序将根据您的输入参数绘制一个“大”字")
    return 0

def inputStartx():
    while True:
        try:
            startX=input("请输入起始横坐标\n按q返回主菜单")
            if startX=='q':
                break
            else:
                startX=int(startX)
                break
        except ValueError:
            print("输入错误！请重新输入！错误类型4") 
    return startX

def inputStarty():
    while True:
        try:
            startY=input("请输入起始纵坐标\n按q返回主菜单")
            if startY=='q':
                break
            else:
                startY=int(startY)
                break
        except ValueError:
            print("输入错误！请重新输入！错误类型4")  
    return startY

def inputSize():
    while True:
        try:
            size=input("请输入字体大小（建议200）\n按q返回主菜单")                       
            if size=='q':
                break
            else:
                size=int(size)
                break
        except ValueError:
            print("输入错误！请重新输入！错误类型4") 
    return size

def inputcolor():
    while True:
        try:
            color=input("请输入颜色\n按q返回主菜单")
            break
        except ValueError:
            print("输入错误！请输入正确的颜色！") 
    return color

def getInput():
    flag=0
    a=inputStartx()
    if a=='q':
        flag=1
        return flag,0,0,0,0
    b=inputStarty()
    if b=='q':
        flag=1
        return flag,0,0,0,0
    c=inputSize()
    if c=='q':
        flag=1
        return flag,0,0,0,0
    d=inputcolor()
    if d=='q':
        flag=1
        return flag,0,0,0,0
    return flag,a,b,c,d 

def Init(color):
    while True:
        try:
            pen_init(25,color,2)
            break
        except Exception:
            color=input("输入错误！请输入正确的颜色！")
    return 0
def run_Da():
    printIntro()
    flag=0
    flag,startX,startY,size,color=getInput()
    if flag==1:
        return
    Init(color)
    print("开始绘制：")
    drawDa(size,startX,startY)
    print("绘制完成")
    return 0
