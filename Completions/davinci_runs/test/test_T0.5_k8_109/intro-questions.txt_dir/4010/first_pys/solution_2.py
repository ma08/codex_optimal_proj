


def check_palindrome(sub_seq):
    return sub_seq[0] == sub_seq[-1] and sub_seq[1] == sub_seq[-2]


def is_palindrome(seq):
    return check_palindrome(seq) or (len(seq) > 3 and is_palindrome(seq[1:-1]))


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = list(map(int, input().split()))
        if is_palindrome(seq):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()