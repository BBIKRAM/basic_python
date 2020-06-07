from abc import ABC,abstractmethod
class InvalidOpereationErroe(Exception):
    pass 
class Stream(ABC):
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
    @abstractmethod     #ALL IT SUB CLASSES MUSST HAVE 
    def read(self):
        pass
class fileStream(Stream):
    def read(self):
        print("reading data for a file")
class networkStream(Stream):
    def read(self):
        print("reading data form a network")
class canteenStream(Stream):
    def read(self):
        print("reading for canteen stream")
m= canteenStream()
m.read()
