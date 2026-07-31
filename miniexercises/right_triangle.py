n=int(input("enter the number of rows:\n"))
m=1

for i in range(n):
    for j in range(m):
        print("*",end=" ")
    m+=1
    print()