ls=[]
even=0
odd=0
size=int(input("Enter the size of the list:"))
for i in range(0,size):
    element=int(input("Input the elements:"))
    ls.append(element)
for i in range(0,size):
    if(ls[i]%2==0):
        even=even+ls[i]
    else:
        odd=odd+ls[i]
print("The sum of even numbers in the list is:",even)
print("The  usm of odd numbers in the list is:",odd)
if(even>odd):
    diff=even-odd
    print("The difference between even and odd numbers is:",diff)
else:
    diff=odd-even
    print("The difference between odd and even number is:",diff)