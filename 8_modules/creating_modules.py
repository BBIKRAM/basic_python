from app import bank,money # specific objects from objects
#consider as a bad practice 
# from app import *
import app  #entire modules as an objects
#in case of modules is in another folder the we need to creat a fill __init__.py
#and to import
# from functions.sales import calc_tax,whaterver
#or
# from ecommerce import sales
#and to acccess just sales.any  
print(dir(sales))
#to know the objects defined
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)