

def main():
    n, a = map(int, input().split())
    e = sorted(list(map(int, input().split())), reverse=True)
    count = 0
    for i in range(n):
        if a >= e[i]:
            a -= e[i]
            count += 1
        else:
            break
    print(count)

main()
