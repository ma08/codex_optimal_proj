

def main():
    """Train the model"""
    cap, sta = map(int, raw_input().split())
    flag = 0
    for _ in range(sta):
        lft, ent, wait = map(int, raw_input().split())
        if cap - lft + ent < 0 or cap - lft + ent - wait < 0:
            flag = 1
            break
        cap = cap - lft + ent - wait
    if flag == 1:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()
