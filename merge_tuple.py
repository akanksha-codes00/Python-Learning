list1=[]
list2=[]
print("Enter 3 numbers for first Tuple:")
for i in range(3):
    num=int(input("Enter number:"))
    list1.append(num)
print("Enter 3 numbers for second Tuple:")
for i in range(3):
    num=int(input("Enter number:"))
    list2.append(num)
t1=tuple(list1)
t2=tuple(list2)
merged=t1+t2
print("First Tuple:",t1)
print("Secons Tuple:",t2)
print("Merged Tuple:",merged)

