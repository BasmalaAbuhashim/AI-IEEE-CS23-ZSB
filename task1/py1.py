lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)
lst.sort()
print(lst[-2])
print(lst[1])
