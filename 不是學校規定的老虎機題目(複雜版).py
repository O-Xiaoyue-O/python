import random
import time
while True:
    print('歡迎玩老虎機')
    end1=input('輸入exit即可結束遊戲,按下enter再抽一次')
    if end1=='exit':
        break
    laba1=['7','apple','banana','6']
    laba={'7':10000,'apple':500,'banana':1000,'6':5000}
    a1=random.choice(laba1)
    print('\n'+a1)
    time.sleep(0.5)
    a2=random.choice(laba1)
    print(a1+' '+a2)
    time.sleep(0.5)
    a3=random.choice(laba1)
    print(a1+' '+a2+' '+a3)
    time.sleep(1)
    if a1==a2 and a2==a3:
        money=laba[a1]*laba[a2]*laba[a3]
    elif a1==a2 and a2!=a3:
        money=laba[a1]*laba[a2]+laba[a3]
    elif a1!=a2 and a2==a3:
        money=laba[a1]+laba[a2]*laba[a3]
    else:
        money=laba[a1]+laba[a2]+laba[a3]
    print('You win money:'+str(money)+'\n')
