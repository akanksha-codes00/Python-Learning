ls=[]
sum=0
size=int(input("Input the siz of list:"))
for i in range(0,size):
    element=int(input("Input the element:"))
    ls.append(element)
for i in range(0,size):
        sum=sum+ls[i]
print("Sum of all elements is given by:",sum)