

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    distances.sort()

    for i in range(n):
        if distances[i] + p * (i + 2) > distances[i + 1]:
            print(distances[i] + p * (i + 2))
            break
    else:
        print(distances[-1] + p * (n + 1))

if __name__ == "__main__":
    main()
