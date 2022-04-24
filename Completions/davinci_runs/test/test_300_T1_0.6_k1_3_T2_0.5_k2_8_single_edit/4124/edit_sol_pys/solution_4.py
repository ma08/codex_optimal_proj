#!/usr/bin/python3

import os
import sys
import time
import datetime

#get the file name
fileName = input("Enter the file name: ")

#check if the file exists
if os.path.exists(fileName) == False:
	print("File does not exist")
	sys.exit()

#get the file stats
fileStats = os.stat(fileName)

#print the file stats
print("File Name: ", fileName)
print("File Size: ", fileStats.st_size)
print("Last Modified: ", time.ctime(fileStats.st_mtime))
print("Created: ", time.ctime(fileStats.st_ctime))

#get the file size
fileSize = os.path.getsize(fileName)

#check the file size
if fileSize > 1024:
	print("File size: ", fileSize//1024, "KB")
else:
	print("File size: ", fileSize, "bytes")

#get the file modified time
modTime = time.ctime(os.path.getmtime(fileName))

#get the current date and time
currentDT = datetime.datetime.now()

#get the file created time
createTime = time.ctime(os.path.getctime(fileName))

#convert the file modified time to datetime format
modDT = datetime.datetime.strptime(modTime, "%a %b %d %H:%M:%S %Y")

#convert the file created time to datetime format
createDT = datetime.datetime.strptime(createTime, "%a %b %d %H:%M:%S %Y")

#calculate the time difference between the file created time and file modified time
timeDiff = modDT - createDT

#print the time difference
print("Time Difference: ", timeDiff)

#check if the file was modified in the current year
if modDT.year == currentDT.year:
	print("File was modified in the current year")
else:
	print("File was not modified in the current year")

#check if the file was modified in the current month
if modDT.month == currentDT.month:
	print("File was modified in the current month")
else:
	print("File was not modified in the current month")

#check if the file was modified in the current day
if modDT.day == currentDT.day:
	print("File was modified in the current day")
else:
	print("File was not modified in the current day")
