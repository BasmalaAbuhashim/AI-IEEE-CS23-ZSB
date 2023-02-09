def sortt_list(val):
    
    
    val.sort()
    
def ret_target(val,target):
    sortt_list(val)
    arr = []
    
    for i in range(len(val)):
        if(val[i] == target):
            arr.append(i)
    print(min(arr),max(arr))
      
try:
    val = list(map(int,input("enter the list of numbers: ").split(",")))
except:
    print("Enter an integer!!!")
target = int(input("enter the target: "))
ret_target(val,target)
