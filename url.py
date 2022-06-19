import requests

from urlextract import URLExtract


def getHTMLText(url):   #获取网页文本
    try:
        r = requests.get(url, timeout=30)       # 获取文本
        r.raise_for_status()        #处理网络异常
        r.encoding = 'utf-8'        # 转码
        return r.text
    except:
        return ""

def getURL(text):   #从网页文本中提取URL
    try:
        extractor = URLExtract()            
        urls = extractor.find_urls(text)    #从text中读取url
        if len(urls) !=0: 
            print(urls)
        return urls
    except:
        return ""
        
isGo=True

def getURLs(urln):   #递归函数
    global isGo
    flagn = 0
    for i in range(len(urln)):
        if isGo==False:     #层层阻止，直到跳出递归
            return
        txt = getHTMLText(urln[i])     #读取urln的文本
        url1 = getURL(txt)             #文本中抽取url
        if url1 != [] and  url1 != "": 
            # print(url1)
            flagn = input("是否继续检索下一层？\nq.退出\n其他任意键继续")
            if flagn=="q":
                print("ready to exit")
                isGo =False     #满足条件
            else:    
                print("ready to continue")
                getURLs(url1)
        # else:
        #     print("该页无url")

def searchURL(url):         #检索url函数
    print("开始检索...")
    text = getHTMLText(url)
    urls = getURL(text)
    getURLs(urls)       #进入递归

def information():
    print("您已进入爬虫程序，该程序将爬取指定网站的超链接\n")

def inputURL():
    while True:
        try:
            url= input("请输入url:")
            break
        except Exception:
            print("请输入正确url!")
    return url

def my_url():
    information()
    url = inputURL()
    searchURL(url)
    return 0