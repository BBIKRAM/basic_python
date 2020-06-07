class Point:
    #these are instance method
    def __init__(self,x,y):
    #it is magic method it is called automatically by 
    #python interpeter when we create the new object
        self.x =x
        self.y=y
    def draw(self):
        print(f"({self.x},{self.y})")
    #this is class method
    @classmethod
    def zero(cls):
        return cls(1,2)
# point= Point(0,0)
point= Point.zero()
point.draw()        