import turtle
import time
def drawGap():    #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):    #绘制单管数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.left(45)
    turtle.fd(5)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(5)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(5)
    turtle.right(135)
#    turtle.penup()
    turtle.fd(47)
#    turtle.pendown()
    drawGap()
    
def drawDigitXie(digit):
    
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)     #1
    turtle.right(100)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)     #2
    turtle.right(80)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)     #3
    turtle.right(100)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)       #4
    
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)       #5
    turtle.right(80)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)       #6
    turtle.right(100)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)       #7
    turtle.right(80)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
def drawDigitZheng(digit):
    
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)     #1
    turtle.right(90)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)     #2
    turtle.right(90)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)     #3
    turtle.right(90)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)       #4
    
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)       #5
    turtle.right(90)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)       #6
    turtle.right(90)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)       #7
    turtle.left(90)
    turtle.penup()
    turtle.fd(20)

def drawDate(script,date):   #date为日期，格式为‘%Y-%m=%d+’

    turtle.pencolor("blue")
    try:
        for i in date:
            if(i=='年'):
                turtle.write('年',font=("Arial",18,"normal"))
                turtle.pencolor("green")
                turtle.fd(40)
            elif i=='月':
                turtle.write('月',font=("Arial",18,"normal"))
                turtle.fd(40)
            elif i=='日':
                turtle.write('日',font=("Arial",18,"normal"))
                turtle.goto(-300,0)
                turtle.right(90)
                turtle.fd(150)
                turtle.left(90)
            elif(i=='时'):
                turtle.write('时',font=("Arial",18,"normal"))
                turtle.pencolor("green")
                turtle.fd(40)
            elif i=='分':
                turtle.write('分',font=("Arial",18,"normal"))
                turtle.fd(40)
            elif i=='秒':
                turtle.write('秒',font=("Arial",18,"normal"))                

            else:
                if script==1:
                    drawDigitZheng(eval(i))
                elif script==2:
                    drawDigitXie(eval(i))
                else:
                    print("script error")
    except NameError:
        print("输入格式错误")

def inputForm():
    while True:
        try:
            form=int(input("显示数字还是时间？\n1.数字\n2.时间\n0.返回主菜单"))
            if(form==1 or form==2 or form==0):
                break
            else:
                print("请输入正确的数值！")
        except Exception:
            print("输入错误！请重新输入！错误类型1")
    return form
    
def inputScript():
    while True:
        try:
            script=int(input("选择字体：\n1.正体\n2.斜体\n0.返回主菜单"))
            if(script==1 or script==2 or script==0):
                break
            else:
                print("请输入正确的数值！")
        except Exception:
            print("输入错误！请重新输入！错误类型2") 
    return script

def getInput():
    flag=0
    a=inputForm()
    if a==0:
        flag=1
        return flag,0,0
    b=inputScript()
    if b==0:
        flag=1
        return flag,0,0
    return flag,a,b 

def printIntro():
    print("您已进入绘制数码管程序，该程序可根据您的输入参数绘制当前时间和任意正整数")

def Init():
    turtle.setup(1000,600,0,0)
    turtle.speed(100)
    turtle.seth(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)

def drawSeg(form,script):
    if form==1:
        num=input("\n请输入一个正整数：")
        drawDate(script,num) 
    elif form==2:      
        drawDate(script,time.strftime('%Y年%m月%d日%H时%M分%S秒',time.gmtime()))
    else:
        return

def run_seg7():
    printIntro()
    flag=0
    flag,form,script=getInput()
    if flag==1:
        return
    Init()
    drawSeg(form,script)
    return 0
#    drawDate('abc')
