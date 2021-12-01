i=1
j=1
for i in range(1,10):
    for j in range(1,10):
        if i*j<10:
            k=' '+str(i*j)
            print(str(i)+'x'+str(j)+'='+k,end=' ')
        else:
            print(str(i)+'x'+str(j)+'='+str(i*j),end=' ')
        if j==9:
            print('')