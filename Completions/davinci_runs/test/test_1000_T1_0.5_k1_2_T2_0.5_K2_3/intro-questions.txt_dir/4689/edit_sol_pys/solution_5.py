
def main():
    k, n = map(int, input().split())
    al = list(map(int, input().split()))
    al.append(al[0] + k)

    min_dist = k
    for i in range(n):
        dist = al[i + 1] - al[i]
        if dist < min_dist:
            min_dist = dist

    print(min_dist)


if __name__ == '__main__':
    main()
