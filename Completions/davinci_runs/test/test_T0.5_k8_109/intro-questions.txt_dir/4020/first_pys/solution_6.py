

# get input
start = input().split(":")
finish = input().split(":")

# convert input to ints
start = [int(x) for x in start]
finish = [int(x) for x in finish]

# determine if the contest ends on the same day it starts
if finish[0] < start[0]:
    finish[0] += 24

# determine the number of minutes the contest lasts
if finish[1] < start[1]:
    finish[1] += 60
    finish[0] -= 1

minutes = finish[0]*60 + finish[1] - start[0]*60 - start[1]

# determine the number of minutes to add to the start time to get to the midpoint
minutes = int(minutes/2)

# determine the new hour and min
hour = (start[0] + int(minutes/60))%24
min = (start[1] + minutes)%60

# print the result
print(str(hour).zfill(2) + ":" + str(min).zfill(2))