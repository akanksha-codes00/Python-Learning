number=int(input("Enter the number:"))
Min=9
while(number!=0):
    digit=int(number%10)
    if(digit<Min):
        Min=digit
    number=int(number/10)
print("Minimum Digits=",Min)
