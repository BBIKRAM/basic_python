 # WHERE FINALLY OR CLOSING OF FILE IS NOT NEEDED
try:
    with open("with_in_exception.py") as file:
        print("file opened")
    age = int(input("a:"))
except (ValueError,SyntaxError):
    print("please enter the valid age")