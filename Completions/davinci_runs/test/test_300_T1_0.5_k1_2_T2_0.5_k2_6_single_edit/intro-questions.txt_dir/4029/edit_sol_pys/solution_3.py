def main():
    n = [int(i) for i in input()]
    n.reverse()
    for i in range(len(n)):
        n[i] += n[i - 1] if i else 0
    res = 0
    for i in range(len(n)):
        if not n[i] % 25:
            res += 1
    print(res)

if __name__ == '__main__':
    main()
