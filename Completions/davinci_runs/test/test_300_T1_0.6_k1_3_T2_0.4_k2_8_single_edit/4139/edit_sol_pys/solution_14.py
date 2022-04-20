

def sgsn(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    print(sgsn(n))
