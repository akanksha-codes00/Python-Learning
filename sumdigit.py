number=int(input("Enter the number:"))
sum=0
while(number!=0):
    digit=int(number%10)
    sum=sum+digit
    number=int(number/10)
print("Sum of Digits=",sum)    