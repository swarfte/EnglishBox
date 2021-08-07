import webScript as WS
import Transform as TF

def start():
    WS.SaveWord(WS.GetEveryDayEnglish())#*獲取每日生字,把每日生字存入Word
    TF.CreateLibrary() #*把Word的生字轉換為中英對照的字典並傳入Library中

if __name__ == "__main__":
    start()