numbers=[]
for i in range(5):
    num=int(input("Enter a number:"))
    numbers.append(num)
t=tuple(numbers)
num=int(input("Enter a number to count its occurrences in the tuple:"))
print("tuple:",t)
print("Frequency of",num,"in the tuple is:",t.count(num))