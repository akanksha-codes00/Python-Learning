number=int(input("Enter the number:"))
print("Extracting digit from the number is:")
while(number!=0):
    digit=number%10
    print(digit)
    number=int(number/10)
