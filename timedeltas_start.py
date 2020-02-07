# Example file for working with timedelta objects

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
  # Construct a basic timedelta and print it
  print(timedelta(days=365,hours=5, minutes=1))
    
  # print today's date
  now=datetime.now()
  print("today is: ",str(now))
  
  # print today's date one year from now
  print("one year from now it will be:" +str(now+timedelta(days=365)))
  
  # calculate timedelta that uses more than one argument
  print("In 2 days and 3 weeks, it will be " + str(now + timedelta(days=2,weeks=3)))
  
  # calculate the date 1 week ago, formatted as a string
  t=datetime.now()  - timedelta(weeks=1)
  s=t.strftime("%A %B %d, %Y")
  print("One week ago it was :", s)
  
  ### How many days until April Fool's Day
  today = date.today()
  afd = date(today.year,4,1)

  if afd< today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year+1)
  time_to_afd = afd-today
  print("It's just ",time_to_afd.days, "days until April Fool's Day")
  
if __name__ == '__main__':
  main()