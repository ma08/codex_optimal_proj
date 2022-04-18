
def main():
    cases = int(input())
    for i in range(cases):
        n = int(input())
        s = input()
        if n % 2 == 1:
            print("-1")
        else:
            c = 0
            for i in range(n // 2):
                if s[i] != s[n // 2 + i]:
                    c += 1
            print(c)

main()
