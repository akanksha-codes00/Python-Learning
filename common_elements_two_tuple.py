t1=tuple(map(int,input("Enter first tuple numbers:").split()))
t2=tuple(map(int,input("Enter second tuple numbers:").split()))
common=()
for n in t1:
    if n in t2 and n not in common:
        common+=(n,)
print("First tuple:",t1)
print("Second tuple:",t2)
print("Common elements:",common)