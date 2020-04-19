from datetime import date
from datetime import datetime
from datetime import time
# Basic understanding of Date and Time in Python 

today = date.today()
dt_time = datetime.now()

print("Current date =", today)
print("Current date =",dt_time)

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Assiging date and time values to variables
a = date(2019, 4, 13)
print(a)

# time(hour = 0, minute = 0, second = 0)
t = time()
print("t =", t)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

''' Output
Current date = 2020-04-18
Current date = 2020-04-18 23:48:25.076642
Current year: 2020
Current month: 4
Current day: 18
2019-04-13
t = 00:00:00
b = 11:34:56
c = 11:34:56
d = 11:34:56.234566
'''

print("hour =", b.hour)
print("minute =", b.minute)
print("second =", b.second)
print("microsecond =", b.microsecond)

# current date and time
now = datetime.now()

st = now.strftime("%H:%M:%S")
print("time:", st)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

''' Output
hour = 11
minute = 34
second = 56
microsecond = 0
time: 23:51:16
s1: 04/18/2020, 23:51:16
s2: 18/04/2020, 23:51:16
'''

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

''' Output
date_string = 21 June, 2018
date_object = 2018-06-21 00:00:00
'''