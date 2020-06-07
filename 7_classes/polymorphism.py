from abc import ABC,abstractmethod
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass
class TextBox(UIControl):
    def draw(self):
        print("testbox")
class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")
def draw(controls):
    for control in controls:
        control.draw()

ddl = TextBox()
ddl2 = DropDownList()
print(isinstance(ddl,UIControl))
# print(ddl2.draw())
draw([ddl,ddl2])


#DUCK TYPING only looks for existences