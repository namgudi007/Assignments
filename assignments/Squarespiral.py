# n = int(input("Enter the number of rows: "))
# m = int(input("Enter the number of columns: "))
# arr = [[0 for i in range(n)]for j in range(m)]
# print("Enter the array elements")
# for i in range(n):
#     for j in range(m):
#         arr[i][j] = int(input())
arr = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
m = 3
n = 3
x = m
y = n
print(arr)
if(n*m >= 1):
    print(arr[0][0])
c = 0
while(c != x/2 or c != y/2):
    for i in range(1, m-c):
        print(arr[c][i])
    for j in range(c+1, n-c):
        print(arr[j][m-1-c])
    for i in range(m-2-c, -1+c, -1):
        print(arr[n-1-c][i])
    for j in range(n-2-c, c, -1):
        # print("j: ", +, j, +, "c: "+c)
        print(arr[j][c])
    c = c+1

exit()
