number=int(input("Enter the number:"))
i=1
factorial=0
while(i<=number):
    factorial=factorial*i
    i=i+i
print("Thhe Factorial of the number is:",factorial)