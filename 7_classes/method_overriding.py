class Animal:
    def __init__(self):
        print("animals constructor")
        self.age =1
    def eat(self):
       print("eat") 
class Fish(Animal):
    def __init__(self):
        print("fish constructor")
        self.weight=3
        super().__init__()
    #MAIN PURPOSE OF SUPER IS TO PREVENT __INIT__ CONSTRUTOR TO OVER WRITE ON PREVIOUS ONE
    def swim(self):
        print("swim")

m= Fish() 
print(m.age)
print(m.weight)

