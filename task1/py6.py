dict1 = { }
val =input("enter values :").split(",")
for i in val:
    name,age = i.split(":")
    dict1[name] = age
print(dict1)
