numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
x=int(input("Enter a number to find its frequency in the tuple:"))
print("Tuple:",t)
print("Frequency of",x,"in the tuple:",t.count(x))
