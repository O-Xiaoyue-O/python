for i in range(3):
    print('請輸入度數')
    b='電費是:'
    a=int(input())
    if a<=100:
        a=a*10
        print(b+str(a))
    elif a>100 and a<=200:
        a=a*20
        print(b+str(a))
    elif a>200:
        a=a*30
        print(b+str(a))