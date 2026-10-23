numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
unique=sorted(set(t),reverse=True)
if len(unique)>=2:
    print("Tuple:",t)
    print("Second Largest:",unique[1])
else:
    print("Second largest number does not exist.")