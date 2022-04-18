

def main():
    """Train"""
    cap, sta = map(int, input().split())
    flag = 0
    for _ in range(sta):
        left, enter, wait = map(int, input().split())
        if cap - left + enter < 0 or cap - left + enter - wait < 0:
            flag = 1
            break
        cap = cap - left + enter - wait
    if flag == 1:
        print("impossible", end="")
    else:
        print("possible", end="")

if __name__ == "__main__":
    main()
