# Example file for working with Calendars


# import the calendar module
import calendar

def main():

  # create a plain text calendar
  c = calendar.TextCalendar(calendar.SUNDAY)
  st = c.formatmonth(2019,12,0,0)
  print (st)
  
  # create an HTML formatted calendar
  hc = calendar.HTMLCalendar(calendar.MONDAY)
  st = hc.formatmonth(2019,12)
  print (st)
  
  #loop over the days of a month
  #zeroes mean that the day of the week is in an overlapping month
  for i in c.itermonthdays(2019,12):
    print (i)
	
  #The Calendar module provides useful utilities for the given locales,
  # such as the names of the days an months in both full and abbreviated forms
  for name in calendar.month_name:
    print(name)
  for day in calendar.day_name:
    print(day)
  
  #Calculate days based on a rule: Ex 1st Friday of every month
  print("Team meetings will be on first Friday of each month on:")
  
  for m in range(1,13):
    cal = calendar.monthcalendar(2020,m)
    weekone=cal[0]
    weektwo=cal[1]
	
    if weekone[calendar.FRIDAY]!=0:
	  meetday = weekone[calendar.FRIDAY]
    else:
	  meetday = weektwo[calendar.FRIDAY]
	  
    print ("%10s %2d" % (calendar.month_name[m],meetday))
	
	
	
if __name__ == "__main__":
  main()