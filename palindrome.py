number=int(input("Enter the number:"))
number2=number
count=0
while(number!=0):
  digit=int(number%10)
  count=count*10+digit
  number=int(number/10)
if(count==number2):
    print("Given number is Palindrome")
else:
   print("Given number is not Palindrome")