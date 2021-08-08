import webScript as WS
import Transform as TF
import practice as PT

def start():
    WS.SaveWord(WS.GetEveryDayEnglish())#*獲取每日生字,把每日生字存入Word
    TF.CreateLibrary() #*把Word的生字轉換為中英對照的字典並傳入Library中
    mode = str(input("中文:1 英文:2 退出:0 請選擇: "))
    value = PT.CreateData(PT.getValue())
    if mode == 1 :
        PT.Chinesequiz(PT.getChinese(value[0]),value[1])
    elif mode == 2:
        PT.Englishquiz(PT.getEnglish(value[0]),value[1])
    else:
        pass
    
    
if __name__ == "__main__":
    start()