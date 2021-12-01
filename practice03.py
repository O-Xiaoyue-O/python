a=[70,22,30,57,24,68,33,41]
b=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]>a[j]:
            b=a[j]
            a[j]=a[i]
            a[i]=b
print(a)