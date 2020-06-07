from datetime import datetime
import time

dt1 = datetime(2018,1,2)
print(dt1)
dt2 = datetime.now()
print(dt2)
dt =datetime.strptime("2018/01/02","%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2>dt1)