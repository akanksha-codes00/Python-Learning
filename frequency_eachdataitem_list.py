count=0
ls=[]
size=int(input("Enter the szie of list:"))
for i in range(0,size):
    element=int(input("Input the elements:"))
    ls.append(element)
for i in range(0,size):
    for j in range(0,size):
      if(ls[i]==ls[j]):
        count=count+1
    print(ls[i],"occurs",count,"times in the list")
    count=0