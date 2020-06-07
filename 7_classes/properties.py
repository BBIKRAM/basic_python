# class Product:
#     def __init__(self,value):
#         self.__set_value(value)
# # 
#     def __get_value(self):
#         return self.__value
#     def __set_value(self,value):
#         if value < 0:
#             raise ValueError("cant be less then 0")
#         self.__value = value
#     value = property(__get_value,__set_value)
# product =Product(23)
# product.value=-1
# print(product.value)
class Product:
    def __init__(self,value):
        self.price=value   
    @property
    def price(self):
        return self.__value
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("cant be less then 0")
        self.__value = value
product =Product(23)
print(product.price)
