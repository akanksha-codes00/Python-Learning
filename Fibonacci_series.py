number=int(input("Enter a number:"))
firstno=0
secondno=1
print("Fibonacci series up to", number, "terms is:")
print(firstno,secondno,end=" ")
for i in range(1,number+1):
    nextno=firstno+secondno
    firstno=secondno
    secondno=nextno
    print(nextno,end=" ")