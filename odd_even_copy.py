ls=[]
odd=[]
even=[]
size=int(input("Enter the size of list:"))
for i in range(0,size):
    element=int(input("enter the element:"))
    ls.append(element)
for i in range(0,size):
    if(ls[i]%2==0):
        even.append(ls[i])
    else:
        odd.append(ls[i])
print("Odd copy of the list is:",odd)
print("even copy of the list is:",even)
