def ADDItem():
    ls=[]
    size=int(input("Enter the size of the list:"))
    for i in range(0,size):
        element=int(input("Input the elemnts:"))
        ls.append(element)
    sum=0
    for i in range(0,size):
      sum=sum+ls[i]
    print("The su of the elements in the list is:",sum)
ADDItem()
