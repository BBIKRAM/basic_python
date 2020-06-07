import random
import string

print(random.random())
print(random.randint(1,23))
# print(random.choices([1,2,3,4]))
# print(random.choices([1,2,3,4],k=3))
# print("".join(random.choices("abcedges",k=3)))


print(string.ascii_letters)
print("".join(random.choices(string.digits + string.ascii_letters,k=9)))


numbers = [1,2,3,4]
random.shuffle(numbers)
print(numbers)