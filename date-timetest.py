import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.strftime("%A"))

# d = datetime.date(2026,8,24)
# print(d)
# print(type(d))
# print(d.day)
# print(d.year)

# dt = datetime.datetime(2026,8,24 ,22,15,0)
# print(dt)
# # print(type(dt))
# # print(dt.day)
# # print(dt.year)
# # print(dt.hour)

# print(dt.strftime("%d/%m/%Y"))
# print(dt.strftime("%d/%B/%Y"))
# print(dt.strftime("%A/%B/%Y"))

# print(dt.strftime("%I:%M %p"))

# s ="20/8/2026"
# dt =datetime.datetime.strptime("20/8/2026","%d/%m/%Y")
# print(dt.date())

now = datetime.datetime.now()
print(now)
tomorow = now+ datetime.timedelta(days =1)
# print(tomorow)
# day = tomorow -now
# print(day.days)
last_week = now - datetime.timedelta(weeks =1)
print(last_week)
five_hours_later = now + datetime.timedelta(hours=5)
print(five_hours_later)
