

"""
Solution
"""

def main():
    X = int(input())
    N = int(input())
    megabytes = X

    for _ in range(N):
        megabytes -= int(input())

    print(megabytes)

if __name__ == '__main__':
    main()
