import json #*用寫讀取數據
import random as rd #*生成隨機數

def ask (file = "./Library.json"):
    with open(file) as word :
        data = json.load(word)#*按json的格式加載word文件到變量data中

    #&分類
    Chinese = data["中文"] #*中文生字
    English = data["英文"] #*英文生字

    #D = {"a" : 1}
    Dictionary = dict() #*創建一個空字典
    Dictionary_length = len(English)#*獲取有多少個英文單詞
    for x in range(Dictionary_length):
        Dictionary[Chinese[x]] = English[x]

    ran_num = rd.randint(0,Dictionary_length - 1)
    
    print(Dictionary)

if __name__ == "__main__":
    ask()
    