def test1(arr):
    b=arr[i]
    arr[i]=arr[a]
    arr[a]=b
arr=[50, 30, 90, 10, 70]
for i in range(len(arr)):
    for a in range(len(arr)):
        if arr[i]<arr[a]:
            test1(arr)
print(arr)