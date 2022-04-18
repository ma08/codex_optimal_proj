

def main():
    """main"""
    cap, _ = map(int, raw_input().split())
    for _ in range(int(input())):
        left, entered, waited = map(int, raw_input().split())
        cap += left
        cap -= entered
        if cap < 0 or waited > 0 and cap == 0:
            print "impossible"
            return
    print "possible"

if __name__ == "__main__":
    main()
