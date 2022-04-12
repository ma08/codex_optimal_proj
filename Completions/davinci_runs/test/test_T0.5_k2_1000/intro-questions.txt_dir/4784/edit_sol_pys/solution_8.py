

"""
Solution
"""

def main():
    x = int(input())
    n = int(input())
    mb = x * 1024
    for i in range(n):
        mb = mb - int(input())
    print(mb)

if __name__ == '__main__':
    main()
