from logging import exception
from operator import truediv
import seg7
import Da
import hesh
import dic
import soccer_manager
import compiler
import url
import sys
def printIntro():
    menu0 = '''
            主菜单
    ==========================
    1：绘图程序

    2：哈希函数

    3：7段数码管

    4：查找保留字

    5：足球经理

    6：网络爬虫

    7：语法分析器

    0：退出程序
    ==========================
    '''
    print(menu0,end=" ")
# 绘图
def myDraw():
    Da.run_Da()
    returnToMain()   
    return 0    
# 哈希
def myHesh():
    hesh.run_hash()
    returnToMain()
    return 0
# 数码管
def mySeg():
    seg7.run_seg7()
    returnToMain()
    return 0

# 查找保留字
def mydic():
    dic.run_dic()
    returnToMain()
    return 0
# 足球经理
def mysoccer():
    soccer_manager.run_soccer()
    returnToMain()
    return 0
def myurl():
    url.my_url()
    returnToMain()
    return 0
def mycompiler():
    compiler.run_compiler()
    returnToMain()
    return 0
#   返回主函数
def returnToMain():
    while True:
        try:
            sellect2 = int(input('按0返回主菜单\n'))
            if sellect2 == 0:
                break
            else:
                print('输入错误!请重新输入！')
        except ValueError:
            print('输入错误!请重新输入！')
    return 0
#   运行函数
def run_menu():
    while True:
        printIntro()
        try:
            sellect1 = int(input('请输入菜单号：'))
            if sellect1 == 1:
                myDraw()
            elif sellect1 == 2:
                myHesh()
            elif sellect1 == 3:
                mySeg()
            elif sellect1 == 4:
                mydic()
            elif sellect1 == 5:
                mysoccer()    
            elif sellect1 == 6:
                myurl()    
            elif sellect1 == 7:
                mycompiler()    
            elif sellect1 == 0:
                print('谢谢使用！')
                break
            else:
                print('输入错误！请重新输入！')
        except ValueError:
            print('请输入正确的菜单号！')
    return 0
                
def main():
    run_menu()
    return 0
main()