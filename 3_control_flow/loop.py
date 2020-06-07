# for number in range(1,10,2):
#     print("message" , number,number * "?")
 
successfull = True
for number in range(3):
    print("print")
    if successfull:
        print("successfull")
        break
else:
    print("message send fail even after trying 3 times")
