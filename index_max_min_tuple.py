numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
maximum=max(t)
minimum=min(t)
print("Tuple:",t)
print("Maximum number:",maximum)
print("Maximum index:",t.index(maximum))
print("Minimum number:",minimum)
print("Minimum index:",t.index(minimum))