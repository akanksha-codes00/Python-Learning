sum=0
number=int(input("Enter the number of terms:"))
for i in range(1, number+1):
    values=int(input("Enter the value:"))
    sum=sum+values
    average=sum/number
print("The  average of the given values is:", average)