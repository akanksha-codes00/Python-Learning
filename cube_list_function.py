def cube(n):
    c=0
    for i in range(1,n+1):
        c=n*n*n
    return c
ls=[]
R=0
size=int(input("Enter the size of the list:"))
for i in range(0,size):
    R=cube(i)
    ls.append(R)
print(ls)