n = int(input("Enter n: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("\n")
# next
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         for k in range(1, i+1):
#             print(k, end="  ")
#     print("\n")
# next
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         for k in range(1, i+1):
#             print(k, end="")
#         print(end=" ")
#     print(end="  ")
#     for j in range(1, i+1):
#         for k in range(i, 0, -1):
#             print(k, end="")
#         print(end=" ")
#     print(end="  ")
#     print("\n")
# next
for i in range(1, n+1):
    for s in range(1, n-i+1):
        print(end="  ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    for s in range(1, n-i+1):
        print(end="  ")
    print("\n")
