number=int(input("Enter the number="))
sum=0
square=number*number
while(square>0):
    digit=square%10
    sum=sum+digit
    square=square//10
if(sum==number):
    print("Entered Number is Neon Number")
else:
    print("Entered Number is Not a Neon Number")