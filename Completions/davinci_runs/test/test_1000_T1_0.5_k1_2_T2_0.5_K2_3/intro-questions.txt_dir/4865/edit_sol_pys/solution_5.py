
    class Time:
        def __init__(self, hour, minute):
            self.hour = hour
            self.minute = minute
        def __repr__(self):
            return str(self.hour)+" "+str(self.minute)
test_cases = int(input())
for i in range(test_cases):
    roll, minutes, hour, minute = input().split()
    minutes = int(minutes)
    hour = int(hour)
    minute = int(minute)
    if roll == "F": #if rolling forward
        if minute + minutes >= 60:
            hour += 1
            minute = minute + minutes - 60
        else:
            minute += minutes
    if roll == "B": #if rolling back
        if minute - minutes < 0:
            hour -= 1
            minute = minute - minutes + 60
        else:
            minute -= minutes
    if hour == 24: #if hour is 24, reset to 0
        hour = 0
    if hour < 0: #if hour is negative, set to 23
        hour = 23
    print(Time(hour, minute))
