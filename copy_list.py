ls=[]
copy=[]
size=int(input("Enter the size of list:"))
for i in range(0,size):
    element=int(input("Enter the elememt:"))
    ls.append(element)
for i in range(0,size):
  if(ls[i]%2==0):
    copy.append(ls[i])
print("Copied list of even elements is:",copy)