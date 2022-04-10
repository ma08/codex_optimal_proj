

def check_wall_height(lst):
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            return False
    return True

def check_bricks_height(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False

def check_bricks_height_sum(lst):
    sum_ = 0
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            sum_ += abs(lst[i] - max(lst))
    return sum_

def check_bricks_height_sum2(lst):
    sum_ = 0
    max_ = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_:
            continue
        else:
            sum_ += abs(max_ - lst[i])
    return sum_

def main():
    n = int(input())
    lst = list(map(int, input().split()))
    if check_wall_height(lst):
        print("YES")
    elif check_bricks_height(lst):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
