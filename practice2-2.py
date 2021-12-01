a,b=input('請輸入2個數字,以空格隔開(EX:5 8):').split()
a=int(a)
b=int(b)
if a>b:
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            answer=i
            break
else:
    for i in range(b,0,-1):
        if a%i==0 and b%i==0:
            answer=i
            break
print(answer)