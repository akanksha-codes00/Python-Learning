number=int(input("Enter the number:"))
sum=0
product=1
while(number>0):
    digit=number%10
    sum=sum+digit
    product=product*digit
    number=number//10

if(sum==product):
    print("Entered Number is Spy Number!")
else:
    print("Entered Number is Not a Spy Number!")