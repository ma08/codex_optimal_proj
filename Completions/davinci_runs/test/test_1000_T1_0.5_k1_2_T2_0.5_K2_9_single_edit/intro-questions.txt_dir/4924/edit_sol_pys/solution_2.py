

import sys

cur_time = sys.stdin.readline().strip().split(':')  # read in current time
exp_time = sys.stdin.readline().strip().split(':')  # read in expected time

# convert to seconds
cur_time = int(cur_time[0])*3600 + int(cur_time[1])*60 + int(cur_time[2])  # convert to seconds
exp_time = int(exp_time[0])*3600 + int(exp_time[1])*60 + int(exp_time[2])  # convert to seconds

# if the expected time is less than current time, add 24 hours
if exp_time < cur_time:  # if the expected time is less than current time, add 24 hours
    exp_time += 24*3600  # add 24 hours

# convert back to hh:mm:ss format
exp_time = exp_time - cur_time  # get the time difference between expected and current time
hours = exp_time//3600  # get the number of hours
minutes = exp_time%3600//60  # get the number of minutes
seconds = exp_time%3600%60  # get the number of seconds

# print out the result
print(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))  # print out the result
