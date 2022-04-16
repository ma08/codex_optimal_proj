

def check_fit(w, h, match):
    if match <= w or match <= h:
        return "DA"
    else:
        return "NE"


def run():
    n, w, h = [int(i) for i in raw_input().split()]

    for i in range(n):
        match_length = int(raw_input())
        print(check_fit(w, h, match_length))


if __name__ == '__main__':
    run()
