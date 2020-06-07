from timeit import timeit
code1="""
def age(x):
    if x<=0:
        raise ValueError("please enter the no greater than 0")
    else:
        print(x)
try:
    age(7)
except ValueError as error:
    print(error)
"""
code2="""
def age(x):
    if x<=0:
        return None
    else:
        print(x)
y=age(3)
if y== None:
    pass
"""

print("code1",timeit(code1,number=1000))

print("code2",timeit(code2,number=1000))
# 