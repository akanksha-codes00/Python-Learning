numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
even_count=0
for num in t:
    if(num%2==0):
        even_count+=1
print("Tuple:",t)
print("Count of even numbers in the tuple:",even_count)