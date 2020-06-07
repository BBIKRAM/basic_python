def fuzz_buzz(input):
    if (input%3==0) and (input % 5==0):
        print("fuzzbuzz")
    elif (input%3==0) or (input % 5==0):
        if input%3 ==0:
            print("fuzz")
        print("buzz")
    print(input)
fuzz_buzz(8)