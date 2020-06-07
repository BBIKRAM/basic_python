import numpy as np


# 
# array = np.array([ [1,2,5,4],[2,3,3,3] ])
# print(array)
# print(type(array))
# print(array.shape)


# array = np.zeros((2,3),dtype = int)
# print(array) 

# array = np.ones((2,3),dtype = int)
# print(array)
 
# array = np.full((2,3),4,dtype = int)
# print(array)


# array = np.random.random((2,3))
# print(array)
# # print(array[1,2])
# # print(array >0.2)
# print(array[array > 0.2])
# print(np.sum(array))        #round,floor etc


first = np.array([1,2,3])
second = np.array([2,3,1])
print(first + second)
print(first + 2)