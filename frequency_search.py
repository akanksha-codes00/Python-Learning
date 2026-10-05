ls=[]
size=int(input("Input the size of list:"))
for i in range(0,size):
    element=int(input("Input the element:"))
    ls.append(element)
    
search=int(input("Input the element to search:"))
count=0
for i in range(0,size):
    if(ls[i]==search):
        count=count+1
print("The element",search,"is found",count,"times in the list.")