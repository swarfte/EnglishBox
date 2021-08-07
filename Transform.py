import json

def CreateLibrary(root="./Word.json",save="./Library.json"):
    with open(root, "r+") as use:#*讀取每日英文
        change = json.load(use)
        with open(save, "r+") as old:#*讀取練習庫
            old_data = json.load(old)
            for k,v in change.items():#*對每個新的生字進行檢查
                check = True #*用作檢測
                for x in range(len(old_data["中文"])):
                    if k == old_data["中文"][x]:
                        check = False
                if check == True:#*沒有重覆則加入新的生字
                    old_data["中文"].append(k)
                    old_data["英文"].append(v)               
                    
    print("目前數據庫的內容")
    print(change)
    print(old_data)
    
    with open(save,"w",encoding="utf-8") as new_data:#*寫入新的檔案
        json.dump(old_data, new_data,ensure_ascii=False)
    
if __name__ == "__main__":
    CreateLibrary()