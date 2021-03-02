#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  filename = "textfile.txt"
  if path.exists(filename):
    # get the path to the file in the current directory
    src = path.realpath(filename)
    
    # let's make a backup copy by appending "bak" to the name
    dest = src +".bak"
    
    # copy over the permissions, modification times, and other info
    # shutil.copy(src, dest)
    # shutil.copystat(src, dest)
    # rename the original file
    # os.rename(src, "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write(filename)
      newzip.write(filename+".bak")
      
if __name__ == "__main__":
  main()
