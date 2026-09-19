term=int(input("Enter the term:"))
firstno=0
secondno=1
print("Fibonacci series is:")
print(firstno,secondno, end=" ")
i=1

while(i<=term):
    nextno=firstno+secondno
    firstno=secondno
    secondno=nextno
    print(nextno, end=" ")
    i=i+1

