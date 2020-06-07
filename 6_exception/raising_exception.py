def age(x):
    if x<=0:
        raise ValueError("please enter the no greater than 0")
    else:
        print(x)
try:
    age(0)
except ValueError as error:
    print(error)
