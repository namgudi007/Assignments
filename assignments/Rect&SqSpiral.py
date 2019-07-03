import numpy as np

m = int(input("Enter no of rows"))
n = int(input("Enter no of columns"))
b = m
d = n
elements = list(map(int, input().split()))
arr = np.array(elements).reshape(m, n)
print(arr)
a = 0
c = 0

while(a < b and c < d):
    for i in range(c, d):
        print(arr[a][i])
    a = a+1
    for i in range(a, b):
        print(arr[i][d-1])
    d = d-1
    if(a < b):
        for i in range(d-1, c-1, -1):
            print(arr[b-1][i])
        b = b-1
    if(c < d):
        for i in range(b-1, a-1, -1):
            print(arr[i][c])
        c = c+1

exit()
