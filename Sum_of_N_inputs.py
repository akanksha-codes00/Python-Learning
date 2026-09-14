sum=0
number=int(input("Enter the number of inputs:"))
for i in range(1,number+1):
    value=float(input("Enter the value:"))
    sum=sum+value
print("Sum of", number, "inputs is:", sum)