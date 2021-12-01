import random
low=0
high=100
times=0 #計算次數
answer=random.randint(0,100)
#print(answer) #用來確認random的產生
print('歡迎來到終極密碼,範圍為0到100')
while(True):
    user=int(input('請輸入數字:'))
    if user>high or low>user:
        print('ERROR,你輸入的範圍超過或小於原本的range,正確的range為'+str(low)+'到'+str(high))
    else:
        if answer==user:
            break
        if answer>=user:
            times+=1
            low=user
            print('範圍已變更,變更為:'+str(low)+' to '+str(high))
        elif user>=answer:
            times+=1
            high=user
            print('範圍已變更,變更為:'+str(low)+' to '+str(high))
times+=1
print('恭喜你,終極密碼是:'+str(answer))
print('你總共猜測了'+str(times)+'次')