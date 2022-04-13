
# SOLUTION for https://www.codechef.com/problems/CHEFZOT

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    max_len = 0
    cur_len = 0
    for i in range(n):
        if arr[i] != 0:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 0
    print(max_len)

if __name__ == "__main__":
    main()
