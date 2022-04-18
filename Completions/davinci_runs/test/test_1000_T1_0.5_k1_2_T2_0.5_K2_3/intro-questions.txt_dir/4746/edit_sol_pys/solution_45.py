
def main():
    """Train"""
    cap, sta = map(int, input().split())  # capacity and stations
    for _ in range(sta):  # number of stations
        left, enter, wait = map(int, input().split())  # people left, people enter, waiting time
        if cap - left + enter < 0 or cap - left + enter - wait < 0:  # if capacity is less than 0
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()
