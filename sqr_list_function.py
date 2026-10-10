def Sqr(n):
    s=0
    for i in range(1,n+1):
        s=n*n
    return s
ls=[]
R=0
size=int(input("Enter the size of the list:"))
for i in range(0,size):
    R=Sqr(i)
    ls.append(R)
print(ls)