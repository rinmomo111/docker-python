import datetime
print(datetime.date.today())

print(datetime.datetime.now())

today = datetime.date.today()
print(today.year)
# １日前
print(today - datetime.timedelta(days=1))

print(today.strftime('%Y年%m月%d日'))
print(today.strftime('%Y/%m/%d'))

