lst = []
output_list = []
n = int(input("enter number of elements: "))
for i in range(0,n):
    val =int(input())
    lst.append(val)
val1 =int(input())
for item in range(n-val1, n): 
    output_list.append(lst[item]) 
      
for item in range(0, n - val1):  
    output_list.append(lst[item]) 
print(output_list)
