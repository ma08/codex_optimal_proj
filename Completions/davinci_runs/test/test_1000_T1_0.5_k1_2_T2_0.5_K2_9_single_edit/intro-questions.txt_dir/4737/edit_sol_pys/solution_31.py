

def main():
    n = int(input())
    for i in range(n):
        p = int(input())
        times = list(map(int, input().split()))
        times = times[p:] + times[:p]
        max_solved = 0
        min_penalty = 0
        remaining = 300
        for t in times:
            if remaining >= t:
                remaining -= t
                max_solved += 1
                min_penalty += t
            else:
                break
        print(max_solved, min_penalty)

if __name__ == "__main__":
    main()
