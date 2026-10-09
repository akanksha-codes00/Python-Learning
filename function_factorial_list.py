def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
ls=[]
R=0
size=int(input("Enter the size of the list:"))
for i in range(0,size):
    R=fact(i)
    if(R==0):
        ls.append(1)
    else:
        ls.append(R)
print(ls)