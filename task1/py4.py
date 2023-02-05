lst = []
n = int(input("enter number of elements: "))
for i in range(0,n):
    val =int(input())
    lst.append(val)
val1 =int(input())
for i in range(0,n):
    for j in range(i,n):
        if lst[j]+lst[i] == val1:
            print(i,j)
