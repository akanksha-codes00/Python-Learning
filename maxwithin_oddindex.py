max=0
ls=[]
size=int(input("enter the size of list:"))
for i in range(0,size):
    element=int(input("Input the elements:"))
    ls.append(element)
for i in range(0,size):
    if(i%2!=0):
        if(ls[i]>max):
            max=ls[i]
print("Maximum number in odd indexed elements in the list is:", max)