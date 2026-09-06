principal=float(input("Enter the value of amount:"))
rate=float(input("Enter the value of interest:"))
time=float(input("Enter the value of time:"))
simple_interest=(principal*rate*time)/100
print(f"The simple interest of {principal}, {rate}, {time} is:",simple_interest)