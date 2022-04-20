

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    assert len(numbers) == n
    gcd_map = {}
    for i in range(n):
        for j in range(i + 1, n):
            if gcd_map.get(numbers[i], numbers[j]) > gcd(numbers[i], numbers[j]):
                gcd_map[numbers[i], numbers[j]] = gcd(numbers[i], numbers[j])
                gcd_map[numbers[j], numbers[i]] = gcd(numbers[i], numbers[j])
    min_lcm = float('inf')
    min_lcm_pair = None
    for key in gcd_map:
        if lcm(key[0], key[1]) < min_lcm:
            min_lcm = lcm(key[0], key[1])
            min_lcm_pair = key
    print(min_lcm_pair)

if __name__ == '__main__':
    main()