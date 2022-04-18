

def nop(inp):
    def is_upper(s):
        return s.isupper()

    def is_lower(s):
        return s.islower()

    def is_digit(s):
        return s.isdigit()

    def is_symbol(s):
        if s.isupper() or s.islower() or s.isdigit():
            return False
        else:
            return True

    def is_valid_password(s):
        upper = 0
        lower = 0
        digit = 0
        symbol = 0
        for c in s:
            if is_upper(c):
                upper = 1
            elif is_lower(c):
                lower = 1
            elif is_digit(c):
                digit = 1
            elif is_symbol(c):
                symbol = 1
        return upper + lower + digit + symbol >= 3

    def nop_helper(s):
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if is_symbol(s[i - 1]):
                if i % 4 != 0:
                    dp[i] = min(dp[i], dp[i - 1] + (4 - i % 4))
        return dp[n]

    if not is_valid_password(inp):
        return 6
    else:
        return nop_helper(inp)

def main():
    inp = list(input())
    print(nop(inp))

if __name__ == '__main__':
    main()
