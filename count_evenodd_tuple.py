numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
even=0
odd=0
for num in t:
    if(num%2==0):
        even+=1
    else:
        odd+=1
print("Tuple:",t)
print("Number of even numbers in the tuple:",even)
print("Number of odd numbers in the tuple:",odd)