
def main():
    n, p = map(int, input().split())
    times = list(map(int, input().split()))[p:] + list(map(int, input().split()))[:p]
    max_solved = 0
    penalties = 0
    remaining = 300
    for t in times:
        if remaining >= t:
            remaining -= t
            max_solved += 1
            penalties += t
        else:
            break
    print(max_solved, penalties)

if __name__ == "__main__":
    main()
