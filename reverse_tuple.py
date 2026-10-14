numbers=input("Enter numbers:")
t=tuple(map(int,numbers.split()))
print("Original tuple:",t)
print("Reversed tuple:",t[::-1])