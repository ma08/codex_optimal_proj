

class MarsLaunch():
    def __init__(self, year):
        self.year = year
        self.month = 0

    def isLaunchWindow(self):
        self.month += 1

        if self.month == 1:
            self.month_days = 31
        elif self.month == 2:
            if self.year % 4 == 0:
                self.month_days = 29
            else:
                self.month_days = 28
        elif self.month == 3:
            self.month_days = 31
        elif self.month == 4:
            self.month_days = 30
        elif self.month == 5:
            self.month_days = 31
        elif self.month == 6:
            self.month_days = 30
        elif self.month == 7:
            self.month_days = 31
        elif self.month == 8:
            self.month_days = 31
        elif self.month == 9:
            self.month_days = 30
        elif self.month == 10:
            self.month_days = 31
        elif self.month == 11:
            self.month_days = 30
        elif self.month == 12:
            self.month_days = 31
        else:
            self.month = 0
            self.year += 1
            self.month_days = 0

        if self.month_days == 30:
            return True
        else:

            return False

def main():
    year = int(input())
    launch = MarsLaunch(year)
    while not launch.isLaunchWindow():
        pass
    if launch.year == year:
        print("yes")
    else:

        print("no")

main()
