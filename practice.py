import json #*用寫讀取數據
import random as rd #*生成隨機數
import Tools

def getValue(file = "./Word.json"):
    with open(file) as word :
        data = json.load(word)#*按json的格式加載word文件到變量data中
    return data

def getChinese(value):
    number = Tools.ran_num_list(4)
    Chinese = [x[0] for x in value]
    choose = [Chinese[x] for x in number]
    return choose

def getEnglish(value):
    number = Tools.ran_num_list(4)
    English = [x[1] for x in value]
    choose = [English[x] for x in number]
    return choose

def Chinesequiz(choose,correct):
    link = {"a":0 , "b":1, "c":2 ,"d":3}
    print(f"{correct[1]}的中文是甚麼")
    print(f"a.{choose[0]} b.{choose[1]} c.{choose[2]} d.{choose[3]}")
    ans = input()
    change = link.get(ans)
    if correct[0] == choose[change]:
        print("正確")
    else:
        print("錯誤")
    
def Englishquiz(choose,correct):
    link = {"a":0 , "b":1, "c":2 ,"d":3}
    print(f"{correct[0]}的英文是甚麼") 
    print(f"a.{choose[0]} b.{choose[1]} c.{choose[2]} d.{choose[3]}")
    ans = input()
    change = link.get(ans)
    if correct[1] == choose[change]:
        print("正確")
    else:
        print("錯誤")

def CreateData (data):
    value = [[k,v] for k,v in data.items()]
    num  = rd.randint(0,len(value)-1)
    correct = [value[num][0],value[num][1]]
    return [value,correct]
    

if __name__ == "__main__":
    value = CreateData(getValue())
    mode = int(input())
    if mode == 0:
        Chinesequiz(getChinese(value[0]),value[1])
    else:
        Englishquiz(getEnglish(value[0]),value[1])
    