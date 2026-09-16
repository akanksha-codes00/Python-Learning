sum=0
firstno=0
secondno=1
number=int(input("Enter the number of terms:"))
for i in range(1,number+1):
    nextno=firstno+secondno
    firstno=secondno
    secondno=nextno
    print(nextno, end=" ")
    if(nextno % 2 != 0):
        sum = sum + nextno
    print()
print("Sum of odd terms in the Lucas series is:",sum)
