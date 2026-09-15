limit=int(input("Enter the limit:"))
for i in range(1,limit+1):
    radius=float(input("Enter the radius of sphere:"))
    volume=4/3*3.14*radius*radius*radius
    print("The volume of sphere with radius", radius, "is:", volume)