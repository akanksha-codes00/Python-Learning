numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
print("Original Tuple:",t)
print("Reversed Tuples:",t[::-1])