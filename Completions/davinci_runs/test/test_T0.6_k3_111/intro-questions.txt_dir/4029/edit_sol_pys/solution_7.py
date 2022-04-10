# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


def main():
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    print(beautifulDays(i, j, k))



def beautifulDays(i, j, k):
    count = 0
    for n in range(i, j + 1):
        if abs(n - int(str(n)[::-1])) % k == 0:
            count += 1
    return count


if __name__ == '__main__':
    main()
