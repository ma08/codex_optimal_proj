

def check_fit(w, h, match_length, n):
    for i in range(n):
        if match_length <= w or match_length <= h:
            return "DA"
        else:
            return "NE"


def run():
    n, w, h = [int(i) for i in input().split()]
    match_length = int(input())
    print(check_fit(w, h, match_length, n))


if __name__ == '__main__':
    run()
