#project -2
#calendar
import calendar
year = int(input("Enter year: "))
m=1
print("\n*****CALENDAR*****")
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i <= 12:
    cal.prmonth(year,i)
    i=i+1

