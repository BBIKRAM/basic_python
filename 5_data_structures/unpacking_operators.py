# values = list(range(4))
# second=[3]
# values = [*range(5),*second,*"hello"]
# print(values)
# where the * is used to unpack the values
#  in case of genertor
first = {"x": 1}
second = { "x": 10 , "y":3}
combined ={**first,**second,"z":1}
print(combined)