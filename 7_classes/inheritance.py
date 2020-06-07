class Animal:
    def __init__(self):
        self.age =1
    def eat(self):
       print("eat") 
#animal :parents ,base
#mammal : child, sub
class Fish(Animal):
    def swim(self):
        print("swim")
class Monkey(Animal):
    
    def jump(self):
        print("jump")
m= Fish()
m.eat() 
print(m.age)
print(isinstance(m,object))
print(issubclass(Animal,object))