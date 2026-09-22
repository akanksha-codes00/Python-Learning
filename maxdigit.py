number=int(input("Enter the number:"))
Max=0
while(number!=0):
    digit=int(number%10)
    if(digit>Max):
        Max=digit
    number=int(number/10)
print("Maximum Digit=",Max)
                 