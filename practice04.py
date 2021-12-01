import random
a=''
syswin=0
userwin=0
for games in range(5):
    while True:
        user=input('猜拳遊戲請輸入:')
        if user=='剪刀' or user=='石頭' or user=='布':
            break
        else:
            print('輸入錯誤,請重試')
    a=random.choice(['剪刀','石頭','布'])
    if a==user:
        print('平手')
    elif a=='剪刀' and user=='布':
        print('系統出剪刀,你輸了')
        syswin+=1
    elif a=='石頭' and user=='剪刀':
        print('系統出石頭,你輸了')
        syswin+=1
    elif a=='布' and user=='石頭':
        print('系統出布,你輸了')
        syswin+=1
    elif a=='布' and user=='剪刀': 
        print('系統出布,你贏了')
        syswin+=1