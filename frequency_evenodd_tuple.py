t={10,15,20,25,30,35,40}
even=0
odd=0
for i in t:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("The number of even numbers in the tuple is:",even)
print("The number of odd numbers in the tuple is:",odd)