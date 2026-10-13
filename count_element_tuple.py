t=tuple(map(int,input("Enter the elements of tuple:").split()))
for n in t:
    if n not in t[:t.index(n)]:
        print("The frequency of ",n,"is:",t.count(n))