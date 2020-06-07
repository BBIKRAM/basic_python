# point ={"x": 1, "y":2}
point = dict(x=1,y=2) 
# print(point["x"])
point["x"]=3   #replacing
#adding new
point["m"]=6
print(point)
print(point.get("a")) 
del point["x"]
print(point)
#using loop
# for key in point:
    # print(key,point[key]
for key,value in point.items():
    print(key,value)
    print()