import datetime

print(datetime.datetime.now())

date_obj=datetime.date(2011,8,8)
print(date_obj)
date_time_obj=datetime.datetime(2020,4,5,12,30,9)
print(date_time_obj)
print(date_obj.strftime("%w"))

