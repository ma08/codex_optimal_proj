

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(A):
    # A をソートする
    A.sort()
    # 最大公約数を求める
    gcd_val = A[0]
    for i in range(1, len(A)):
        gcd_val = gcd(gcd_val, A[i])
    # 取り除く数を求める
    if gcd_val == 1:
        return 1
    remove_num = 1
    while remove_num * gcd_val <= 10**9:
        remove_num += 1
    remove_num -= 1
    return remove_num * gcd_val

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(A))