sum=0
average=0
ls=[]
week=7
for i in range(0,week):
    element=int(input("Input the elemets:"))
    ls.append(element)
for i in range(0,week):
    sum=sum+ls[i]
print("The sum of the elements in the list is:",sum/week)