

def main():
    """Train"""
    cap, sta = map(int, input().split())
    flag = False
    for _ in range(sta):
        lft, ent, wait = map(int, input().split())
        if cap - lft + ent < 0 or cap - lft + ent - wait < 0:
            flag = True
            break
        cap = cap - lft + ent - wait
    if flag:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()
