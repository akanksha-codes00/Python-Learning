odd=2
firstno=3
secondno=5
upperlimit=int(input("Enter the upper limit:"))
print("The odd numbers between", firstno, "and", upperlimit, "are:")
print(firstno,end=" ")
print(secondno,end=" ")
for i in range(1,upperlimit+1):
    nextno=firstno+secondno
    firstno=secondno
    secondno=nextno
    print(nextno, end=" ")
    if(nextno % 2 !=0):                                                                                                                   
        odd = odd+1
print()    
print("The odd numbers between", firstno, "and", upperlimit, "are:",odd )