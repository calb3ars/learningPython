#!/usr/bin/python
import time;  # This is required to include time module.

localtime = time.asctime(time.localtime(time.time()) )

# print "Local current time:", localtime

import calendar
cal = calendar.month(2017, 5)
# print "This Month's calendar"
# print cal

# print(time.clock() )
# time.sleep(5)
# print(time.clock() )

# cali = calendar.calendar(2017, w=4, l=2, c=4)
# print(cali)

# monthcal = calendar.monthcalendar(2017, 5)
# print(monthcal)

wkdy = calendar.weekday(2017, 5, 17)
print(wkdy)
