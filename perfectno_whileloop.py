
number=int(input("Enter the number: "))
sum=0
i=1
while(i<number):
    if(number%i==0):
        sum=sum+i
    i=i+1
if(sum==number):
    print("The nunber is a perfect number")
else:
    print("The number is not a perfect number")