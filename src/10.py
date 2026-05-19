import calendar

date_input = input().split()
month = int(date_input[0])
day = int(date_input[1])
year = int(date_input[2])

day_num = calendar.weekday(year, month, day)

day_name = calendar.day_name[day_num].upper()

print(day_name)
