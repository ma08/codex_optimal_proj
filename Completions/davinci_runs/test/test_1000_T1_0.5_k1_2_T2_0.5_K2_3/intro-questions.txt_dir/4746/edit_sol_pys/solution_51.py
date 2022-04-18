

def main():
    """Train and Wait"""
    cap, sta = map(int, input().split()) #cap is capacity, sta is station
    flag = 0
    for _ in range(sta):
        lft, ent, wait = map(int, input().split())
        if cap - lft + ent < 0 or cap - lft + ent - wait < 0:
            flag = 1
            break
        cap = cap - lft + ent - wait #cap is capacity, lft is left, ent is enter, wait is wait
    if flag == 1:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()
