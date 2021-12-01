import random
number1=random.randint(1,49)
number2=random.randint(1,49)
number3=random.randint(1,49)
number4=random.randint(1,49)
number5=random.randint(1,49)
number6=random.randint(1,49)
test2=[0]*6
while(True):
    user=input()
    if len(user)==6:
        break
    else:
        print('error')
test1 = [int(a) for a in str(user)]
for i in range(6):
    for a in range(5):
        str(test1[a])
        str(test2[a])
    test2[i]=test1[i]+test1[i+1]
    print(test2)
    if i==5:
        break