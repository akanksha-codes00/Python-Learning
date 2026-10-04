ls=[]
odd=0
size=int(input("Enter the size of list:"))
for i in range(0,size):
    element=int(input("enter the element:"))
    ls.append(element)
print("The value of Odd index elements in the list are:")
for i in range(0,size):
     if(i %2!=0):
        print(ls[i])
