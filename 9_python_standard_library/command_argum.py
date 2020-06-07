import sys

if len(sys.argv)==1:
    print("useges:python3 command_arg <password>")
else:
    password = sys.argv[1]
    print("password",password)