

def main():
    _, p = map(int, input().split())
    times = list(map(int, input().split()))
    times = times[p:] + times[:p] # rotate
    max_solved = 0
    total_penalty = 0
    remaining = 300
    for t in times:
        if remaining >= t:
            remaining -= t
            max_solved += 1
            total_penalty += t
        else:
            break
    print(max_solved, total_penalty)

if __name__ == "__main__":
    main()
