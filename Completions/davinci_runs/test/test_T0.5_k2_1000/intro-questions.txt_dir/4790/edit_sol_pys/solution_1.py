
import sys

def main():
    data = sys.stdin.read().splitlines()[0]
    print(data)
    # b_count = 0
    # w_count = 0
    # for i in range(len(s)):
    #     if s[i] == 'B':
    #         b_count += 1
    #     else:
    #         w_count += 1
    # if b_count == w_count or b_count - w_count == 1 or w_count - b_count == 1:
    #     print(1)
    # else:
    #     print(0)

if __name__ == "__main__":
    main()
