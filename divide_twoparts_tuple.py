numbers=[]
for i in range(6):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
mid=len(t)//2
first=t[:mid]
second=t[mid:]
print("Original Tuple:",t)
print("First Half:",first)
print("Second Half:",second)