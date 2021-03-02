#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("today's date is ", today)

  # print out the date's individual components
  print("date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Week day number: ", today.weekday())
  days = ["Mon", "Tues", "Wed", "Thus", "Fri", "Sat", "Sun"]
  print("today is day: ",days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()

  print("Date time is ", today)

  # Get the current time
  time = datetime.time(today)

  print("Time is ", time)
 

  
if __name__ == "__main__":
  main();
  