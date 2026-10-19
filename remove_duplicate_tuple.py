numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
unique=tuple(set(t))
print("Original Tuple:",t)
print("Unique Tuple:",unique)