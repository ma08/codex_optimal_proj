

def check_fit(w, h, match):
    if match <= w or match <= h or match <= (w**2 + h**2)**0.5:
        return "YES"
    else:
        return "NO"


def run():
    n, w, h = [int(i) for i in input().split()]

    for i in range(n):
        match_length = int(input())
        print(check_fit(w, h, match_length))


if __name__ == '__main__':
    run()
