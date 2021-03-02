#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type
  filename="textfile.txt"
  print("Items exists: " + str(path.exists(filename)))
  print("Item is a file: " + str(path.isfile(filename)))
  print("Item is a Dir: " + str(path.isdir(filename)))
  # Work with file paths
  print("Item path: " + str(path.realpath(filename)))
  print("Item path: " + str(path.split(path.realpath(filename))))
  
  # Get the modification time
  t = time.ctime(path.getmtime(filename))
  print("Modified time: "+str(t))
  print("Modified time: " + str(datetime.datetime.fromtimestamp(path.getmtime(filename))))
  
  # Calculate how long ago the item was modified

  td = datetime.datetime.now() - datetime.datetime.fromtimestamp((path.getmtime(filename)))

  print ("It has been " + str(td) + " since the file was modified")
  print("It has been " + str(td.total_seconds()) + " since the file was modified")

if __name__ == "__main__":
  main()
