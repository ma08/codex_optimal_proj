

def main():
    """Train and Wait"""
    cap, sta = map(int, input().split())
    flag = 0
    for _ in range(sta):
        lft, ent, wait = map(int, input().split())
        if cap - lft + ent < 0 or cap - lft + ent - wait < 0:  # if the train has to wait
            flag = 1
            break
        cap = cap - lft + ent - wait  # update the capacity
    if flag == 1:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()
