limit=int(input("Enter the limit:"))
print("Tebles till limit:")
for i in range(1,limit+1):
    for j in range(1,11):
        table=i*j
        print(table,end=" ")
    print()