# def greet():
#     print("hello this is print")

# greet()


#passing arguments
# def add(a,b):
#     m=a+b
#     print(m)
# add(3,4)

# def name(first,last):
#     print(f"{first} {last}")
# name("bikram","basnet")

# def add(*numbers):
#     sum= 0
#     for number in numbers:
#         sum+=number
#     return sum
# sum= add(3,4,4,5)
# print(sum)

def save_user(**user):
    print(user)
    print(user["name"])
save_user(id=1,name="bikram")