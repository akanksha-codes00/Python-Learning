def ADDItem(size):
    ls=[]
    for i in range(0,size):
        element=int(input("Input the elemnts:"))
        ls.append(element)
    sum=0
    for i in range(0,size):
            sum=sum+ls[i]
    print("The sum of the elements in the list is:",sum)
m=int(input("Enter the size of the list:"))
ADDItem(m)