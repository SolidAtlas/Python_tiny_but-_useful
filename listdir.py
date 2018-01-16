# Program that will list a directory
# and store the names in a text file

import os

directory = input('Give the name of the directory you wish to strip. Note if no entry the program will default to the directory the python file is currently in.:')
print(directory)

name_of_file = input('Give this file a name: ')

name_of_file = name_of_file + '.txt'

textfile = open( name_of_file , 'w')

if directory == '' or directory == ' ':
  list_of_files = os.listdir()
  print (list_of_files)
else:
  list_of_files = os.listdir(directory)
  print (list_of_files)

do_sort =  input('Do you want the list sorted alphabetically? Y/n: ')

if do_sort == 'Y':
  list_of_files.sort()
  print(list_of_files)
  for item in list_of_files:
    textfile.write('%s\n' % item)
else:
  for item in list_of_files:
    textfile.write('%s\n' % item)

textfile.close()

