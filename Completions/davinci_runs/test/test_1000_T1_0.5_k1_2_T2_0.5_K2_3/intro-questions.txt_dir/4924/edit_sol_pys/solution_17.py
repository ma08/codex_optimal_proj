
import sys

cur_time = sys.stdin.readline().strip().split(':')
exp_time = sys.stdin.readline().strip().split(':')

# convert to seconds
cur_time = int(cur_time[0]) * 3600 + int(cur_time[1]) * 60 + int(cur_time[2])
exp_time = int(exp_time[0]) * 3600 + int(exp_time[1]) * 60 + int(exp_time[2])

# if the expected time is less than current time, add 24 hours
if exp_time < cur_time:
    exp_time += 24 * 3600

# convert back to hh:mm:ss format
exp_time = exp_time - cur_time
hours = exp_time // 3600
minutes = exp_time % 3600 // 60
seconds = exp_time % 3600 % 60

# print out the result
print(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
