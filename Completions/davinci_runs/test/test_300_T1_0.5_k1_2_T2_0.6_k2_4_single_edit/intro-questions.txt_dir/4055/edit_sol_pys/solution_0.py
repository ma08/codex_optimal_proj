
def find_disturbing(a):
    disturbed = []
    for i in range(1, n - 1):
        if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
            disturbed.append(i)
    return len(disturbed)

n = int(input())
a = list(map(int, input().split()))

print(find_disturbing(a))
