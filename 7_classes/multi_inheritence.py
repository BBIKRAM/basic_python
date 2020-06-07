#dont use  multi leve inheritence to much 
# class person:
#     def greet(self):
#         print("hello person")
# class animals:
#     def greet(self):
#         print("hell anials")
# class person_animals(person,animals):
#     pass

# m=person_animals()
# m.greet()

#GOOD EXAMPLE OF
class InvalidOpereationErroe(Exception):
    pass 
class Stream:
    def __init__(self):
        self.opened = False
    def  open(self):
        if self.opened:
            raise InvalidOpereationErroe("file is already open")
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOpereationErroe("file is closed")
        self.opened= False
class fileStream(Stream):
    def read(self):
        print("reading data for a file")
class networkStream(Stream):
    def read(self):
        print("reading data form a network")

m= fileStream()
m.read()

