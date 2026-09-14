number=int(input("Enter the number of sets:"))
for i in range(1,number+1):
    radius=float(input("Enter the radius of circle:"))
    area=3.14*radius*radius
    print("Area of circle with rdius", radius, "is:", area)