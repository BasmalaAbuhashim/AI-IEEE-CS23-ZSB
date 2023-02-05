lst=input().split()
for i in range ( 0,len(lst) ):
    if (lst[i] != lst[-1-i]):
        res = "not-symmetric"
        break
    res = "symmetric"
print(res)
