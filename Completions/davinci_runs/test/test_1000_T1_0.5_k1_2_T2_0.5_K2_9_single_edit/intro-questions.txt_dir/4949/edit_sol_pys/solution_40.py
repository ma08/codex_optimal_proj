

def check_fit(w, h, match):
    if match <= w or match <= h:
        return "DA"
    else:
        return "NE"


def run():
    n, w, h = input().split()
    n = int(n)
    w = int(w)
    h = int(h)

    for i in range(n):
        match_length = int(input())
        print(check_fit(w, h, match_length))


if __name__ == '__main__':
    run()
