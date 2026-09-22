number=int(input("Enter the number:"))
even=0
odd=0
while(number!=0):
    digit=int(number%10)
    if(digit%2==0):
        even=even+1
    else:
        odd=odd+1
number=int(number/10)
print("Total Even=",even)
print("Total Odd=",odd)