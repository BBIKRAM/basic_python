import time
def send_emails():
    for i in range(20000):
        pass
start = time.time()
print(start)
send_emails()
end = time.time()
print(end)
duration = end-start
print(duration)