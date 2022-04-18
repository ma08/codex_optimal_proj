

# My Solution
def solution(n, a):
    while len(a) > 1:
        a.sort()
        attacker = random.randint(0, len(a)-1)
        victim = random.randint(0, len(a)-1)
        if a[attacker] > a[victim]:
            a[victim] = 0
            a = [i for i in a if i != 0]
        else:
            a[attacker] = 0
            a = [i for i in a if i != 0]
    return a[0]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solution(n, a))
