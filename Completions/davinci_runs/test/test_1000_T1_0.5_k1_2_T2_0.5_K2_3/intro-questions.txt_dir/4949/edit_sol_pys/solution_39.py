

def check_fit(w, h, match_length):
    if match_length <= w and match_length <= h:
        return "DA"
    else:
        return "NE"


def run():
    n, w, h = [int(i) for i in input().split()]

    for i in range(n):
        match_length = int(input())
        print(check_fit(w, h, match_length))


if __name__ == '__main__':
    run()
