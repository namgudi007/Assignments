

def trees(e, i, p):
    if(len(i) == 1):
        list1.append(i[0])
    elif(len(i) == 0):
        return("Byee")
    else:
        list1.append(p[0])
        root = p[0]
        j = i.index(root)
        lefti = i[:j]
        print(lefti)
        righti = i[j+1:]
        leftp = p[1:j+1]
        rightp = p[j+1:e]
        trees(len(lefti), lefti, leftp)

        trees(len(righti), righti, rightp)
    return(list1)


list1 = []
e = int(input(""))
i = list(map(int, input().rstrip().split()))
p = list(map(int, input().rstrip().split()))
list1 = trees(e, i, p)
print(list1)
