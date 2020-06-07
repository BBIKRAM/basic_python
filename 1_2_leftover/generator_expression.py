#list
#  values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)
# genrator 
from sys import getsizeof
values = (x * 2 for x in range(1000000))
print("gen:", getsizeof(values))
# in case of list it takes more bytes the generator takes constaant
values = [x * 2 for x in range(1000000)]
print("gn:", getsizeof(values))