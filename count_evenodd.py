number = int(input("Enter the number:"))
even = 0
odd = 0
for i in range(1,number+1):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total even numbers are:",even)
print("Total odd numbers are:",odd)
if(odd>even):
     print("There are more odd numbers than even nunbers")
elif(even>odd):
    print("There are more even numbers than odd nunbers")
else:
    print("There are equal odd and even numbers")