class Text(str):
    def duplicate(self):
        return self+ self
class trackablelist(list):
    def append(self,object):
        print("append called")
        super().append(object)
list = trackablelist()
list.append('4')