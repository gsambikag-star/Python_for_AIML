n=int(input("\nenter the no of rows:\n"))
m=n
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    m-=1
    print()