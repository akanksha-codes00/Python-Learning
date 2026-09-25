count=0
sum=0
for i in range(1,4,1):
    for j in range(1,i+1,1):
        count=count+1
        sum=sum+count
        print(sum,end=" ")
    print()