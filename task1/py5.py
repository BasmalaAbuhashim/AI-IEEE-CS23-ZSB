lst =input("Enter List Of String : ").split()
#print(lst)
fst_h=[]
sec_h=[]

for i in range (0,len(lst)):
    if len(lst[i]) %2==0:
        lstt1=lst[i]
        lstt2=lst[i]
        fst_hal =lstt1[:(len(lst[i])//2)]
        fst_h.append(fst_hal)
        sec_hal =lstt2[(len(lst[i])//2):]
        sec_h.append(sec_hal)
    else:
        fst_hal =lstt1[:(len(lst[i])//2 +1)]
        fst_h.append(fst_hal)
        sec_hal =lstt2[(len(lst[i])//2+1):]
        sec_h.append(sec_hal)
print("First half of list is ",fst_h)
print("Second half of list is ",sec_h)
