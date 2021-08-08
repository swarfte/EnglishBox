import random as rd

#*創造不重覆的隨機亂數
def ran_num_list(num): #*list的長度
    tick = []
    while len(tick) < num:#&限制長度為4,即0~3
        temp = rd.randint(0,3)
        if len(tick) != 0 :
            check = 0 #&用作判斷新的隨機數是否和tick內的相同
            for x in tick : #&用新的隨機數和tick內的數字比較
                if x == temp :
                    check += 1 
            if check == 0 : #&當沒有重覆的時候才加入新的隨機數
                tick.append(temp)
        else:#&當tick的長度為0時,執行初始化
            tick.append(temp)
    return tick