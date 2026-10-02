ls=[]
size=int(input("Enter the size of list:"))

for i in range(0,size):
    element=int(input("Enter the element:"))
    ls.append(element)
print("Even elements in the list are:")
for i in range(0,size):
    if(ls[i]%2==0):
        print(ls[i])
        