

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):  # O(N)
        if (a[i - 1] == 1 and a[i + 1] == 1 and a[i] == 0):  # O(1)
            count += 1
    print(count)



"""
Complexity: O(N)
"""
if __name__ == "__main__":
    main()
