import random
laba1=['7','apple','banana','6']
laba={'7':10000,'apple':500,'banana':1000,'6':5000}
a1=random.choice(laba1)
a2=random.choice(laba1)
a3=random.choice(laba1)
print(a1)
print(a2)
print(a3)
if a1==a2 and a2==a3:
    money=laba[a1]*laba[a2]*laba[a3]
elif a1==a2 and a2!=a3:
    money=laba[a1]*laba[a2]+laba[a3]
elif a1!=a2 and a2==a3:
    money=laba[a1]+laba[a2]*laba[a3]
else:
    money=laba[a1]+laba[a2]+laba[a3]
print('You win money:'+str(money)+'\n')
