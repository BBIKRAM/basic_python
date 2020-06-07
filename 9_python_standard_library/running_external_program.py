import subprocess

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# complete = subprocess.run(["python3","others.py"],capture_output=True,text=True)
# # complete = subprocess.run(["ls","-l"],capture_output=True,text=True)
# print("args",complete.args)
# print("returncode",complete.returncode)
# print("stderr",complete.stderr)
# print("stdout",complete.stdout)



try:

    complete = subprocess.run(["false"],capture_output=True,text=True,check=True)
    print("args",complete.args)
    print("returncode",complete.returncode)
    print("stderr",complete.stderr)
    print("stdout",complete.stdout)
# if complete.returncode!=0:
#     print(complete.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)