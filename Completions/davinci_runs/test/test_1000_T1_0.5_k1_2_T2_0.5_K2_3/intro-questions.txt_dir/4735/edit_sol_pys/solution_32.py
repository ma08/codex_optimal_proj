class MarsLaunch
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def is_launch_window(self):
        if self.year % 4 == 0:
            return self.month == 2 and self.month_days == 29
        return self.month_days == 30

def main():
    year, month = map(int, input().split())
    launch = MarsLaunch(year, month)
    print("yes" if launch.is_launch_window() else "no")

main()
