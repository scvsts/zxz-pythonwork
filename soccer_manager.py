from operator import truediv
from random import random
from tkinter import N
def printIntro():
    print("该程序模拟两个选手A和B的足球比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
    print("程序运行需要环境和选手状态的判定（以1到4之间的小数表示）")
    return 0

def getInputs():
    while True:
        try:
            a=eval(input("请输入选手A的能力值（0-1）："))
            if(a>0 and a<1):
                break
            else:
                print("能力值不在0-1内，，请重新输入！")
        except Exception:
            print("请输入正确的数字！")
    while True:
        try:
            fa=eval(input("请输入选手A的失误概率（0-1）："))
            if(fa>0 and fa<1):
                break
            else:
                print("失误概率不在0-1内，，请重新输入！")
        except Exception:
            print("请输入正确的数字！")     
    while True:
        try:
            weathera=int(input("选手A适合什么天气？\n晴天请输入“1”\n雨天请输入“2”\n多云请输入“3”\n雪天请输入“4”\n"))
            if(weathera==1 or 2 or 3 or 4):
                break
            else:
                print("请重新输入!")
        except Exception:
            print("请输入正确的数字！")          
    while True:
        try:
            b=eval(input("请输入选手B的能力值（0-1）："))
            if(b>0 and b<1):
                break
            else:
                print("能力值不在0-1内，，请重新输入！")
        except Exception:
            print("请输入正确的数字！")
    while True:
        try:
            fb=eval(input("请输入选手B的失误概率（0-1）："))
            if fb>0 and fb<1 :
                break
            else:
                print("失误概率不在0-1内，，请重新输入！")
        except Exception:
            print("请输入正确的数字！")   
    while True:
        try:
            weatherb=int(input("选手B适合什么天气？\n晴天请输入“1”\n雨天请输入“2”\n多云请输入“3”\n雪天请输入“4”\n"))
            if weatherb==1 or 2 or 3 or 4:
                break
            else:
                print("请重新输入!")
        except Exception:
            print("请输入正确的数字！")      
    while True:
        try:
            n=int(input("模拟比赛场次："))
            if(n>0):
                break
            else:
                print("请输入一个正整数！")
        except Exception:
            print("请输入一个正整数！")
    return a,fa,weathera,b,fb,weatherb,n 
    
def power(probA,probB,weatherA,weatherB):
    weatherA,weatherB
    while True:
        try:
            s=eval(input("请于此处选择比赛的天气：\n晴天请输入“1”\n雨天请输入“2”\n多云请输入“3”\n雪天请输入“4”\n"))
            if s==weatherA:
                probA=probA+0.1
            if s==weatherB:
                probB=probB+0.1
                break
            else:
                print("请重新输入!")
        except NameError:
            print("请输入正确的数字！")
    while True:
        try:
            q=eval(input("请判断选手A赛前状态，状态极佳请输入“1”\n状态良好请输入“2”\n状态一般请输入“3”\n状态极差请输入“4”\n"))
            if q==1:
                probA=probA*1.1
                break
            elif q==2:
                probA=probA
                break
            elif q==3:
                probA=probA*0.95
                break
            elif q==4:
                probA=probA*0.8
                break
            else:
                print("请输入正确的数字！")
        except NameError:
            print("请输入正确的数字！")
    while True:
        try:
            p=eval(input("请判断选手B赛前状态，状态极佳请输入“1”\n状态良好请输入“2”\n状态一般请输入“3”\n状态极差请输入“4”\n"))
            if p==1:
                probB=probB*1.1
                break
            elif p==2:
                probB=probB
                break
            elif p==3:
                probB=probB*0.95
                break
            elif p==4:
                probB=probB*0.8
                break
            else:
                print("请重新输入")
        except NameError:
            print("请输入正确的数字！")
    return probA,probB

def simNGames(n,probA,faultA,probB,faultB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,faultA,probB,faultB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB
def gameOver(a,b):
    return a==15 or b==15
def simOneGame(probA,faultA,probB,faultB):
    ran,scoreA,scoreB=0,0,0
    serving="A"
    while not gameOver(scoreA,scoreB):
        ran=random()
        if serving=="A":
            if ran<probA and ran>faultA:
                scoreA+=1
            else:
                serving="B"
        else:
            if ran<probB and ran>faultB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB
def printSummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
    return 0
def run_soccer():
    printIntro()
    probA, faultA, weatherA, probB, faultB, weatherB, n=getInputs()
    probA, probB=power(probA,probB,weatherA,weatherB)
    winsA, winsB=simNGames(n,probA,faultA,probB,faultB)
    printSummary(winsA,winsB)
    return 0