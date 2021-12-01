star=int(input())
a=star-1
for i in range(star):
    b=1+i*2
    print(' '*a+'*'*b)
    a-=1
a+=1
print()

for j in range(star,0,-1):
    c=j*2-1
    print(' '*a+'*'*c)
    a+=1
print()

a=0
for j in range(star,0,-1):
    print(' '*a+'*'*j)
    a+=1