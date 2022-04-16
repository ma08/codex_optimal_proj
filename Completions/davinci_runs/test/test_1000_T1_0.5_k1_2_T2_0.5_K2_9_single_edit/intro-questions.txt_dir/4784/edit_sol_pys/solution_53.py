
"""
Solution
"""

def main():
    X = int(input())
    N = int(input())
    mb = X
    for i in range(N):
        mb -= int(input())
    print(mb)

if __name__ == '__main__':
    main()
