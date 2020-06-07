class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self,what):
        return self.x == what.x and self.y==what.y
    def __gt__(self,other):
         return self.x >= other.x and self.y >= other.y
    #ARTHIMATIC METHOD
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

point= Point(3,2)
other =Point(3,2)
print(point==other)
print(point<other)
sum=point+other
print(sum.x)
#ARTHIMATIC METHOD