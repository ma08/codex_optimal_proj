from sys import stdin

def main():
    S, C, K = map(int, stdin.readline().split())
    D = list(map(int, stdin.readline().split()))
    D.sort()
    machine_count = 0
    for i in range(0, S, C):
        machine_count += 1
        if K == 0:
            continue

        for j in range(i, i + C - 1):
            if abs(D[j] - D[j + 1]) > K:
                machine_count += 1
                break

    print(machine_count)

main()
