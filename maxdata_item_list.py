max=0
ls=[]
size=int(input("Input the size of list:"))
for i in range(0,size):
    element=int(input("Input the element:"))
    ls.append(element)
for i in range(0,size):
    if(ls[i]>max):
        max=ls[i]
print("Maximum element is in the list:",max)