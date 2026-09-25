firstno=0
secondno=1
for i in range(1,4,1):
    for j in range(1,i+1,1):
        nextno=firstno+secondno
        firstno=secondno
        secondno=nextno
        print(nextno,end=" ")
    print()