ls=[]
odd=0
even=0
size=int(input("enter the size of list:"))
for i in range(0,size):
    element=int(input("Input the elements:"))
    ls.append(element)
for i in range(0,size):
    if(ls[i]%2==0):
        even=even+ls[i]
    else:
        odd=odd+ls[i]
print("Total sum of even numbers in the list is:",even)
print("Total sum of odd numbers in the list is:",odd)