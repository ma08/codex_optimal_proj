
#I know this could be done with a lot less code, but it's a very simple problem and I want to get used to using classes

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        return str(self.hours)+" "+str(self.minutes)

test_cases = int(input())
for i in range(test_cases):
    roll, minutes, hours, minutes = input().split()
    minutes = int(minutes)
    hours = int(hours)
    minutes = int(minutes)
    if roll == "F":
        if minutes + minutes >= 60:
            hours += 1
            minutes = minutes + minutes - 60
        else:
            minutes += minutes
    if roll == "B":
        if minutes - minutes < 0:
            hours -= 1
            minutes = minutes - minutes + 60
        else:
            minutes -= minutes
    if hours == 24:
        hours = 0
    if hours < 0:
        hours = 23
    print(Time(hours, minutes))
