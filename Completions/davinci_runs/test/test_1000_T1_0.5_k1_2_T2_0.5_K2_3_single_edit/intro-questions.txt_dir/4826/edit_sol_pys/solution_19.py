
def solve(n):
    return "Alice" if n % 2 == 1 else "Bob"  # 奇数ならAlice、偶数ならBobを返す


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
