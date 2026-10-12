def ADDITEM(n):
    ls=[]
    for i in range(0,n):
        element=int(input("Input the element:"))
        ls.append(element)
    print(ls)
    s=0
    for i in range(0,n):
        s=s+ls[i]
    return s
m=int(input("Enter the size of the list:"))
print(ADDITEM(m))
    