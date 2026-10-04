ls=[]
even=0
odd=0
size=int(input("enter the size of list:"))
for i in range(0,size):
    element=int(input("enter the element:"))
    ls.append(element)
for i in range(0,size):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("The total number of even is:",even)
print("The total number of odd is:",odd)


        