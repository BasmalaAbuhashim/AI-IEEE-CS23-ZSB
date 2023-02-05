# range = max_num - min_num
dict1 = {
    "A":[20,30,100,49],
    "B":[00,199,201,29],
    "C":[40,90,69,18]
}

max_res = 0
'''key = list(dict1.keys())
val = list(dict1.values())'''
for val,val1 in dict1.items():
	
	max_res = max(max_res, max(val1) - min(val1))	
	if max_res == max(val1) - min(val1):
          '''ind = val.index(max_res)
          res = dict1.get(val)'''
          res = val
		
print(res)
