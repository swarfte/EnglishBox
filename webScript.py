import urllib.request as UR
import bs4
import re
import datetime as DT
import json

def GetEveryDayEnglish():
    url = "https://www.englishday.cc/"
    with UR.urlopen(url) as response:
        data = response.read().decode("utf-8")#*獲取html內容

    root = bs4.BeautifulSoup(data, "html.parser")#*按html的格式解碼
    english_native = root.find("div",id = "english_word_box")#*找出關鍵的位置
    english_choose = re.compile(r"\>[a-z]+\<")#*找出關鍵字
    english_word = re.search(english_choose,str(english_native)).group()#*獲取過濾後的字符串
    english_use = english_word[1:-1]#*過濾頭尾

    chinese_native = root.find("h1")
    chinese_use = chinese_native.a.string #*<h1> <a>標籤中的字符串
    output = dict()
    output[chinese_use] = english_use #*生成字典
    today = DT.date.today()#*獲取今日的日期
    
    #*輸出該次爬到的資料
    print(str(today) + "的每日英文單詞")
    print(output)
    
    return output

def SaveEnglishWord(EnglishWord,FileName = "./EnglishWord.json"):
    with open(FileName, "r+",encoding='utf-8') as File:
        native = json.dumps(EnglishWord)#*把單引號轉為雙引號
        data = json.loads(native)#*準備寫入的新資料
        old_data = json.load(File)#*讀取舊資料
        check = 0 #*檢測新舊資料
        for x in old_data.keys():
            if x in data :
                check +=1
        if check == 0 :
            old_data.update(data)#*合併新舊生字
    
    with open(FileName, "w",encoding="utf-8") as File: #*寫入新的資料
        json.dump(old_data,File,ensure_ascii=False)#*禁用ascii碼