# age = int(input("age:"))
# print(age)

try:
    file=open("handling_exception.py")
    age=int(input("a:"))
    num = 2/age
    #multiple error can be described in same exception insted of making one
except (ValueError,ZeroDivisionError,ModuleNotFoundError): 
    print("please int value")
else:
    print("this is shown when try is successfully")
finally:
    file.close()
    

# try:
#     age=int(input("a:"))
# except ValueError as ex:
#     print("please int value")
#     print(ex)
#     print(type(ex))
# else:
#     print("this is shown when try is successfully")