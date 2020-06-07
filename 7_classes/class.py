#class is a blueprint for creating  new objects
#object: instance of a class
class Point:
    monkey = "you"   #it is class level attributes
    def __init__(self,x,y):   #is a special function
        self.x = x #instance attributes
        self.y=y
    def draw(self):
        # print("draw")
        print(f"point:({self.x},{self.y})")
    

# point = Point()
# print(type(point))
# print(isinstance(point,Point))

point= Point(1,2)
point.draw()