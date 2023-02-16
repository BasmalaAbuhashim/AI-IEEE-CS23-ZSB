def mean(lst):
    i = sum(lst)
    if len(lst)!=0:
        med = i/len(lst) 
    return med

def median (lst):
    lst.sort()
    if (len(lst) % 2 == 0):
        fst_med = lst[len(lst)//2]
        sec_med = lst[len(lst)//2+1]
        
        the_med = (fst_med + sec_med)/2
    else:
        the_med = lst[len(lst)//2]
    return the_med

def mode (lst):
    mod = []
    not_mod = []
    for i in lst:
        if i not in not_mod:
            not_mod.append(i)
        else:
            mod.append(i)
    return mod

if __name__ == "__main__":
    while True:
        try:
            lst = list(map(int,input().split()))
            break
        except ValueError:
            print("please enter an integer number: ")
    if(lst):
        print("the mean:%0.3f"%mean(lst))
        print("the median: ",median(lst))
        print("the mode: ",mode(lst))