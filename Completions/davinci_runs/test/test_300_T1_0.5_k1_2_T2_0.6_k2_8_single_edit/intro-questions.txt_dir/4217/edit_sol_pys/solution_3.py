

def main(n, m, k, s):
    foods = [0] * m
    for i in range(n):
        for j in s[i]:
            foods[j-1] += 1
    print(foods.count(n))

if __name__ == '__main__':
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        k = int(input().split()[0])
        s.append(map(int, input().split()))
    main(n, m, k, s)
