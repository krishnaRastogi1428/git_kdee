import time

CurrrentTime_hrs = time.strftime('%H')
CurrrentTime_min = time.strftime('%M')
CurrrentTime_sec = time.strftime('%S')
print(int(CurrrentTime_hrs),":", int(CurrrentTime_min),":", int(CurrrentTime_sec))