# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __eq__(self,other):
#         return self.x == other.x and self.y == other.y
# p1=point(1,2)
# p2=point(1,2)
# print(p1==p2)


from collections import namedtuple
point = namedtuple("point",["x","y"])
p1=point(x=1,y=2)
p2=point(x=1,y=2)
print(p1==p2)