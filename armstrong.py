number=int(input("Enter the number:"))
sum=0
temp=number
while(number!=0):
    digit=int(number%10)
    sum=sum+(digit*digit*digit)
    number=int(number//10)
if(sum==temp):
    print("Entered number is Armstrong Number")
else:
    print("Entered number is Not an Armstrong Number")