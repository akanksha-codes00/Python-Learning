sum=0
count=0
ls=[]
size=int(input("Enter the size of list:"))
for i in range(0,size):
    element=int(input("Input the element:"))
    ls.append(element)
for i in range(0,size):
    if(i%2!=0):
         sum=sum+ls[i]
         count=count+1
         avg=sum/count
print("Average of odd indexed element in the lit is:",avg)
