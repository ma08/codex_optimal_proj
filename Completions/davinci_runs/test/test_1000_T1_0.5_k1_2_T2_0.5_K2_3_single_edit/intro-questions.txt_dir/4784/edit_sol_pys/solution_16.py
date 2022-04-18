

"""
Solution
"""

def main():
    X = int(input())
    N = int(input())
    megabytes = X + 1
    for i in range(N):
        megabytes = megabytes - int(input())
    print(megabytes)

if __name__ == '__main__':
    main()
