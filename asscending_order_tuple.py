numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
sorted_tuple=tuple(sorted(t))
print("Original Tuple:",t)
print("Ascending Order:",sorted_tuple)