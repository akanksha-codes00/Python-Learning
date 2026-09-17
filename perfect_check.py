number=int(input("Enter the number:"))
sum=0
for i in range(1, number):
    if(number%i==0):
        sum=sum+i
if(sum==number):
    print("The number is a perfect number:")
else:
    print("The number is not a perfct number:") 