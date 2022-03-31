

def main():
    n = int(input())  # number of elements
    a = list(map(int, input().split()))  # list of elements
    l = [0 for i in range(101)]  # list of counters
    for i in a:  # counting
        l[i] += 1  # counting
    for i in range(1, 101):  # counting
        l[i] += l[i-1]  # counting
    for i in range(100, 0, -1):  # counting2
        l[i] = l[i-1]  # counting
    l[0] = 0  # counting
    for i in range(1, 101):  # counting
        l[i] += i  # counting
    if l[-1] == n:  # checking
        print("YES")  # checking
    else:  # checking
        print("NO")  # checking

main()
