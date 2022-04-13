"""
Given a number N, print the number of digits in the number and the digits in the number.
"""

def main():
    t = int(input())

    for _t in range(t):
        n = int(input())
        ans = []
        while n > 0:
            ans.append(n % 10)
            n //= 10
        for _i in range(len(ans)):
            if ans[_i] == 0:
                ans[_i] = 10
            else:
                ans[_i] = ans[_i] * (10 ** _i)
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()
