count=0
number=int(input("Enter the number:"))
while(number!=0):
    digit=int(number%10)
    count=count+1
    number=int(number/10)
print("Total digits ",count)
