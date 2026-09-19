term=int(input("Enter the term:"))
firstno=0
secondno=1
print("Fibonacci series is:")
print(firstno, end=" ")
print(secondno, end=" ")
for i in range(1,term+1):
    nextno=firstno+secondno
    firstno=secondno
    secondno=nextno
    print(nextno, end=" ")

