numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
print("Tuple:",t)
print("Largest number in the tuple:",max(t))