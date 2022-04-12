

def main():
    """Train the model"""
    cap, sta = map(int, input().split()) # capacity, stations
    flag = 0
    for _ in range(sta):
        lft, ent, wait = map(int, input().split()) # left, enter, wait
        if cap - lft + ent < 0 or cap - lft + ent - wait < 0: # if capacity is negative, impossible
            flag = 1
            break
        cap = cap - lft + ent - wait
    if flag == 1:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()
